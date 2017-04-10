from game.gameflow.flowstate.repositories import PendingTurnRepository
from game.gameflow.flowstate.factories import TurnFactory

class CurrentTurnProvider(object):

    def __init__(self):
        self.pending_turn_repository = PendingTurnRepository()
        self.turn_factory = TurnFactory()

    def get_or_create_turn(self, game):
        '''Returns current turn or None if game is over'''
        pending_turn = self.__pending(game)
        if pending_turn:
            return pending_turn
        return self.__create(game)

    def __pending(self, game):
        pending_turns = self.pending_turn_repository.get(game)
        if pending_turns:
            if len(pending_turns) > 1:
                raise Exception("More than one active turn in game")
            return pending_turns[0]

    def __create(self, game):
        return self.turn_factory.get_or_create(game)

