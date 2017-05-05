from game.configuration.definitions import LogLevel, LogType
from game.document.documents.turn import Turn
from game.document.seeding.turn_seed_factory import TurnSeedFactory
from game.operation.mutation_adapter import MutationAdapter
from logger import Logger


class TurnFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.turn_seed_factory = TurnSeedFactory()
        self.mutation_adapter = MutationAdapter()

    def create(self, actor_id, phase, mutations):
        self._log_mutations(mutations)
        mutation_data = self.mutation_adapter.to_turn(mutations)
        turn_data = self.turn_seed_factory.create(actor_id, mutation_data)
        turn = Turn(turn_data, parent=phase)
        phase.turns.append(turn)
        return turn

    @staticmethod
    def _log_mutations(mutations):
        if mutations:
            log_message = "Adding queued mutations (count: {}) to new turn.".format(len(mutations))
        else:
            log_message = "No mutations to add to new turn."
        Logger.log(log_message, level=LogLevel.Debug, log_type=LogType.GameLogic)
