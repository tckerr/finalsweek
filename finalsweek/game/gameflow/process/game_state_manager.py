from game.program_api.program_api import ProgramApi


class GameStateManager(object):
    def new(self, player_count):
        api = ProgramApi.new(player_count)
        api.turns.get_or_create_current_turn()
        game_id = self.save(api)
        return game_id, api

    @staticmethod
    def load(game_id, fresh=False):
        # note: requesting_actor_id should be generated from auth user, not passed in request
        api = ProgramApi.from_id(game_id)
        turn = api.turns.get_or_create_current_turn(fresh=fresh)
        if not turn:
            return api, None
        # TODO: assert authenticated user is owner of actor
        return api, turn

    @staticmethod
    def save(api):
        return api.save_game()
