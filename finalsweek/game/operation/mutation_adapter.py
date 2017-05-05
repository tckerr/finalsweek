from game.configuration.definitions import MutationGameflowBinding, LogLevel, LogType
from logger import Logger


class MutationAdapter(object):
    def to_phase(self, mutations):
        return self.__adapt(mutations, MutationGameflowBinding.Phase)

    def to_turn(self, mutations):
        return self.__adapt(mutations, MutationGameflowBinding.Turn)

    @staticmethod
    def __adapt(mutations, binding):
        log_message = "Adding queued mutations (count: {}) to newly created turn.".format(len(mutations))
        Logger.log(log_message, level=LogLevel.Debug, log_type=LogType.GameLogic)
        results = []
        for mutation in mutations:
            mutation.gameflow_binding = binding
            results.append(mutation.data)
        return results
