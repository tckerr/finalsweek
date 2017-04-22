from game.gameflow.flowstate.factories import TurnFactory


class CurrentTurnProvider(object):
    def __init__(self):
        self.turn_factory = TurnFactory()

    def get_or_create_turn(self, api, fresh=False):
        """Returns current turn or None if game is over"""
        pending_turn = self.__pending(api)
        if pending_turn:
            if fresh:
                api.refresh_current_turn(pending_turn.id)
            return pending_turn
        return self.__create(api)

    @staticmethod
    def __pending(api):
        for turn in api.list_turns():
            if turn.completed is None:
                return turn

    def __create(self, api):
        result = self.turn_factory.get_or_create(api)
        return result
