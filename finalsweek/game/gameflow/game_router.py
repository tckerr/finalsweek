from game.factories import GameFactory, ActorFactory
from game.ensurers import GameCreationEnsurer
from game.managers.input.input_manager_resolver import InputManagerResolver
from game.summaries.builders import GameSummaryBuilder
from game.gameflow.current_turn_provider import CurrentTurnProvider

class GameRouter(object):

    def __init__(self):
        self.game_creation_ensurer = GameCreationEnsurer()
        self.game_factory = GameFactory()
        self.actor_factory = ActorFactory()
        self.input_manager_resolver = InputManagerResolver()        
        self.game_summary_builder = GameSummaryBuilder()
        self.current_turn_provider = CurrentTurnProvider(self.take_turn)

    def create(self, player_count):
        self.game_creation_ensurer.ensure()
        game = self.game_factory.create(player_count)
        return self.__build_summary(game)    
    
    def load(self, actor_id, count=0):
        game_id = self.actor_factory.load(actor_id).game_id
        game = self.game_factory.load(game_id)        
        return self.__build_summary(game)    

    def take_turn(self, actor_id, action=None):
        actor = self.actor_factory.load(actor_id)
        turns = actor.turns.filter(completed__isnull=True)
        if not turns:
            raise Exception("Not your turn!")
        if turns.count() > 1:
            raise Exception("More than 1 turn!")
        turn = turns.first()
        self.input_manager_resolver.resolve(turn, action) # true if it did anything        
        return self.load(actor_id)

    def __build_summary(self, game):
        current_turn = self.current_turn_provider.get(game)
        return self.game_summary_builder.build(game, current_turn)

