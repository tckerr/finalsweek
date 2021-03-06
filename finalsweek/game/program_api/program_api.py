from game.document.persistence.caching import GameDocumentCache
from game.document.seeding.game_seed_factory import GameSeedFactory
from game.program_api.actor_api import ActorApi
from game.program_api.card_template_api import CardTemplateApi
from game.program_api.game_deck_api import GameDeckApi
from game.program_api.mutation_api import MutationApi
from game.program_api.phase_api import PhaseApi
from game.program_api.seat_api import SeatApi
from game.program_api.settings_api import SettingsApi
from game.program_api.stage_api import StageApi
from game.program_api.student_api import StudentApi
from game.program_api.turn_api import TurnApi


class ProgramApi(object):
    """ProgramApi is the primary class through which the internal systems retrieve and modify game state"""

    @classmethod
    def from_id(cls, game_id):
        cache = GameDocumentCache()
        cache.load_from_id(game_id)
        return cls(cache)

    @classmethod
    def new(cls, player_count, seed, rules):
        generator = GameSeedFactory()
        game_seed = generator.generate(player_count=player_count, seed=seed, rules=rules)
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
        self.mutations = MutationApi(self)

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
