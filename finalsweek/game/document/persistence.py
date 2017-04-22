from mongo import MongoDbConnector


class GamePersistence(object):
    """GamePersistence is a wrapper around MongoDbConnector specifically for games"""
    _doc_name = "game"

    def __init__(self):
        super(GamePersistence, self).__init__()
        self.mongo_db_connector = MongoDbConnector("finalsweek")

    def load(self, game_id):
        games = list(self.mongo_db_connector.list(self._doc_name, _id=game_id))
        if len(games) == 0:
            raise Exception("Game id '{}' does not exist!".format(game_id))
        elif len(games) > 1:
            raise Exception("More than one game for id '{}' exists!".format(game_id))
        return games[0]

    def insert(self, data):
        return self.mongo_db_connector.insert(self._doc_name, data)

    def replace(self, _id, data):
        success = self.mongo_db_connector.replace(self._doc_name, _id, data)
        if success.matched_count != 1:
            raise Exception("Document was not saved, failed to match on id: {}".format(_id))
        return success
