from game.exceptions import TurnPermissionException
from game.gameflow.process.action_executor import ActionExecutor
from game.gameflow.process.game_state_manager import GameStateManager
from game.interface.digest import DigestProvider


class GameInterface(object):
    def __init__(self):
        self.digest_provider = DigestProvider()
        self.action_executor = ActionExecutor()
        self.game_manager = GameStateManager()

    def create(self, player_count):
        game_id, api = self.game_manager.new(player_count)
        return self.digest_provider.game_info_digest(game_id, api)

    # TODO: requesting_actor_id should be generated from auth user, may need to pull ProgramApi up a level to check this
    def take_turn(self, game_id, requesting_actor_id, action):
        api, turn = self.game_manager.load(game_id)
        if turn.actor_id != requesting_actor_id:
            raise TurnPermissionException("Not your turn!")
        turn = self.action_executor.execute(turn, action, api)
        return self.__save_and_summarize(api, requesting_actor_id, turn)

    def load(self, game_id, requesting_actor_id, fresh=False):
        api, turn = self.game_manager.load(game_id, fresh=fresh)
        return self.__summarize(api, requesting_actor_id, turn, game_id)

    # *~--- Private Methods ----* #

    def __save_and_summarize(self, api, requesting_actor_id, turn):
        game_id = self.game_manager.save(api)
        return self.__summarize(api, requesting_actor_id, turn, game_id)

    def __summarize(self, api, requesting_actor_id, turn, game_id):
        return self.digest_provider.general_digest(game_id, api, turn, requesting_actor_id)
