from sim.engine.systems.game_manager import GameManagerFactory
from sim.engine.ruleset import Ruleset, RulesetFactory

class GameApiAction(object):
    pass

class GameInterface(object):

    def __init__(self):
        self.game_manager_factory = GameManagerFactory()
        self.ruleset_factory = RulesetFactory()

    def create_ruleset(self, max_actors, actions_per_turn, auto_create_ai):
        ruleset = self.ruleset_factory.create(max_actors, actions_per_turn, auto_create_ai)
        return ruleset.id

    def create_game(self, user_ids, ai_slots, ruleset_id):
        game_manager = self.game_manager_factory.create_new(user_ids, ai_slots, ruleset_id)
        return game_manager.game_id


    def submit_action(self, game_id, action):
        game_manager = self.game_manager_factory.load(game_id)
        assert issubclass(action.__class__, GameApiAction)
        
        game_manager.submit_action(action)


class DebugGameInterface(GameInterface):

    def load_game(self, game_id):
        '''ONLY FOR TESTING'''
        return self.game_manager_factory.load(game_id)

    def create_game_debug(self, user_ids, ai_slots, ruleset_id):
        game_id = self.create_game(user_ids, ai_slots, ruleset_id)
        return self.load_game(game_id)
 
