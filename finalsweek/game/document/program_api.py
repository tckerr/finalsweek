from game.document.api.card_template_api import CardTemplateApi
from game.document.api.game_deck_api import GameDeckApi
from game.document.api.phase_api import PhaseApi
from game.document.api.seat_api import SeatApi
from game.document.api.settings_api import SettingsApi
from game.document.api.stage_api import StageApi
from game.document.api.student_api import StudentApi
from game.document.api.turn_api import TurnApi

from game.document.api.actor_api import ActorApi
from game.document.game_document_cache import GameDocumentCache
from game.document.seed_generators import GameSeedGenerator


class ProgramApi(object):
    """ProgramApi is the primary class through which the internal systems retrieve and modify game state"""

    @classmethod
    def from_id(cls, game_id):
        cache = GameDocumentCache()
        cache.load_from_id(game_id)
        return cls(cache)

    @classmethod
    def new(cls, player_count):
        generator = GameSeedGenerator()
        game_seed = generator.generate(player_count=player_count)
        cache = GameDocumentCache()
        cache.load_from_seed(game_seed)
        return cls(cache)

    def __init__(self, cache):
        self._cache = cache
        self.settings = SettingsApi(self)
        self.card_templates = CardTemplateApi(self)
        self.game_decks = GameDeckApi(self)
        self.stages = StageApi(self)
        self.phases = PhaseApi(self)
        self.turns = TurnApi(self)
        self.seats = SeatApi(self)
        self.students = StudentApi(self)
        self.actors = ActorApi(self)

    @property
    def data(self):
        return self._cache.cache

    def save_game(self):
        game_id = self._cache.save()
        return game_id

    def increment_metadata(self, key, value):
        if key not in self.data.metadata:
            self.data.metadata[key] = 0
        self.data.metadata[key] += value
