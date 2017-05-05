from game.configuration.definitions import MutationGameflowBinding, LogLevel, LogType
from logger import Logger


class MutationAdapter(object):
    def to_phase(self, mutations):
        return self.__adapt(mutations, MutationGameflowBinding.Phase)

    def to_turn(self, mutations):
        return self.__adapt(mutations, MutationGameflowBinding.Turn)

    @staticmethod
    def __adapt(mutations, binding):
        results = []
        for mutation in mutations:
            mutation.gameflow_binding = binding
            results.append(mutation.data)
        return results
