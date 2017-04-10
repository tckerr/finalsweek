from game.summaries.builders import GameSummaryBuilder
from game.gameflow.runner import GameRunner
from game.actions import UseActionCardAction
from game.options import TurnOptionBuilder, Perspective


class GameRouter(object):

    def __init__(self):
        self.game_summary_builder = GameSummaryBuilder()
        self.turn_option_builder = TurnOptionBuilder()
        self.game_runner = GameRunner()

    def create(self, player_count):
        game = self.game_runner.create(player_count)
        current_turn = self.game_runner.get_current_turn(game)
        return self.__build_summary(game, current_turn, None)
    
    def load(self, actor_id,):
        game = self.game_runner.load(actor_id)  
        current_turn = self.game_runner.get_current_turn(game)     
        return self.__build_summary(game, current_turn, actor_id)    

    def take_turn(self, actor_id, decisions=None):
        action = UseActionCardAction(actor_id, decisions) if decisions else None
        self.game_runner.take_turn(actor_id, action)  
        return self.load(actor_id)

    def get_turn_options(self, actor_id, decisions):
        game = self.game_runner.load(actor_id)
        current_turn = self.game_runner.get_current_turn(game)
        if current_turn.actor.id != actor_id:
            return None
        return self.turn_option_builder.build(current_turn, decisions)

    def __build_summary(self, game, current_turn, actor_id=None):
        return self.game_summary_builder.build(game, current_turn, perspective=Perspective(actor_id))
