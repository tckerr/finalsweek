from game.document.program_api import ProgramApi
from game.exceptions import GameOverException


class GameStateManager(object):
    def new(self, player_count):
        api = ProgramApi.new(player_count)
        game_id = self.save(api)
        return game_id, api

    @staticmethod
    def load(game_id, fresh=False):
        # note: requesting_actor_id should be generated from auth user, not passed in request
        api = ProgramApi.from_id(game_id)
        turn = api.turns.get_current_turn(fresh=fresh)
        if not turn:
            return api, None
        # TODO: assert authenticated user is owner of actor
        return api, turn

    @staticmethod
    def save(api):
        return api.save_game()