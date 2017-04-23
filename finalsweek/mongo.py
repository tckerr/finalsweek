import settings
from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoDbConnector(object):
    def __init__(self, db_name):
        self._host = settings.credentials.mongo_connection_host
        self._port = settings.credentials.mongo_connection_port
        self._client = MongoClient("{}:{}".format(self._host, self._port))
        self._db = self._client[db_name]

    def list(self, document_type, **kwargs):
        self._fix_id(kwargs)
        cursor = self._db[document_type].find(kwargs)
        for item in cursor:
            yield item

    def insert(self, document_type, document):
        return self._db[document_type].insert_one(document).inserted_id

    def replace(self, document_type, _id, document):
        find_query = {"_id": ObjectId(_id)}
        return self._db[document_type].replace_one(find_query, document)

    def _fix_id(self, kwargs):
        _id = kwargs.get("_id", None)
        if _id and _id.__class__ is str:
            kwargs["_id"] = ObjectId(_id)