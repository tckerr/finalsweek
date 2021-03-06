from game.document.documents.game import Game
from game.document.persistence.connectors import GameDbConnector


class GameDocumentCache(object):
    """GameCache is stateful cache which is the system of record for game state."""

    def __init__(self):
        self._game_db_connector = GameDbConnector()
        self._initialized = False

    @property
    def cache(self):
        return self._cache

    @property
    def game_id(self):
        return self._game_id

    def load_from_seed(self, dictionary):
        self._init(dictionary)

    def load_from_id(self, game_id):
        data = self._game_db_connector.load(game_id)
        self._init(data, game_id)

    def _init(self, data, game_id=None):
        if self._initialized:
            raise Exception("You may only load a cache once.")
        game = Game(data)
        self._cache = game
        self._game_id = game_id
        self._initialized = True

    def save(self):
        if not self._cache:
            raise Exception("You may not save an uninitialized cache.")
        data = self._cache.data
        if self._game_id:
            _id = self._game_id
            self._game_db_connector.replace(self._game_id, data)
        else:
            _id = self._game_db_connector.insert(data)
        return _id
