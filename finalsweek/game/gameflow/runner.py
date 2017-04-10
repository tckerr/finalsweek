from game.factories import GameFactory, ActorFactory
from game.ensurers import GameCreationEnsurer
from game.managers.input.input_manager_resolver import InputManagerResolver
from game.gameflow.flowstate.providers import CurrentTurnProvider
from game.gameflow.action_automater import ActionAutomater

class GameRunner(object):

    def __init__(self):
        self.game_creation_ensurer = GameCreationEnsurer()
        self.actor_factory = ActorFactory()
        self.input_manager_resolver = InputManagerResolver()        
        self.current_turn_provider = CurrentTurnProvider()
        self.action_automater = ActionAutomater(self.take_turn)
        self.game_factory = GameFactory()

    def create(self, player_count):
        #self.game_creation_ensurer.ensure()
        game = self.game_factory.create(player_count)
        return game

    def load(self, actor_id):
        actor = self.actor_factory.load(actor_id)
        return self.game_factory.load(actor.game_id)

    def take_turn(self, actor_id, action=None):
        actor = self.actor_factory.load(actor_id, prefetch="turns")
        turns = list(filter(lambda t: t.completed is None, actor.turns.all()))
        if not turns:
            raise Exception("Not your turn!")
        if len(turns) > 1:
            raise Exception("More than 1 turn!")
        turn = turns[0]
        self.input_manager_resolver.resolve(turn, action) # true if it did anything     

    def get_current_turn(self, game):
        next_turn = self.current_turn_provider.get_or_create_turn(game)
        if self.action_automater.automate_if_needed(next_turn):
            return self.get_current_turn(game)
        return next_turn

