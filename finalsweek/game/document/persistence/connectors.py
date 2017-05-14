from mongo import MongoDbConnector


class GameDbConnector(object):
    """GameDbConnector is a wrapper around MongoDbConnector specifically for Games"""
    _doc_name = "game"

    def __init__(self):
        super(GameDbConnector, self).__init__()
        self.mongo_db_connector = MongoDbConnector("finalsweek")

    def load(self, game_id):
        games = list(self.mongo_db_connector.list(self._doc_name, _id=game_id))
        if len(games) == 0:
            raise Exception("Game id '{}' does not exist!".format(game_id))
        elif len(games) > 1:
            raise Exception("More than one game for id '{}' exists!".format(game_id))
        return games[0]

    def list_summaries(self):
        summary_projection = {
            "_id":                    1,
            "seats.student.actor.id": 1,
            "metadata":               1
        }
        games = list(self.mongo_db_connector.list(self._doc_name, projection=summary_projection))
        return map(self.adapt_game, games)

    @staticmethod
    def adapt_game(game):
        return {
            "id":           str(game["_id"]),
            "metadata": game["metadata"],
            "actors":       [seat["student"]["actor"]["id"]
                             for seat in game["seats"]
                             if "student" in seat
                             and "actor" in seat["student"]]
        }

    def insert(self, data):
        return self.mongo_db_connector.insert(self._doc_name, data)

    def replace(self, _id, data):
        success = self.mongo_db_connector.replace(self._doc_name, _id, data)
        if success.matched_count != 1:
            raise Exception("Document was not saved, failed to match on id: {}".format(_id))
        return success
