from game.configuration.definitions import LogLevel, LogType
from game.operation.factories import MutationFactory
from game.operation.operation_mutator import OperationMutator
from game.scripting.api.program_child_api import ProgramChildApi
from logger import Logger


class MutationApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.mutation_factory = MutationFactory()
        self.operation_mutator = OperationMutator(program_api)

    def remove_mutation(self, mutation_id):
        new_mutations = [m for m in self.data.mutations if m.id != mutation_id]
        assert (len(new_mutations) == len(self.data.mutations) - 1)
        self._log_remove_mutation(mutation_id)
        self.data.mutations = new_mutations

    def create_and_register(self, mutation_template, **exports):
        mutation = self.mutation_factory.create_from_template(mutation_template, **exports)
        self.data.mutations.append(mutation)
        self._sort_mutations()
        message = "Creating mutation {}".format(mutation.id)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
        return mutation

    def mutate(self, operation):
        return self.operation_mutator.mutate(operation, self.data.mutations)

    def _sort_mutations(self):
        self.data.mutations = sorted(self.data.mutations, key=lambda m: m.priority, reverse=True)

    @staticmethod
    def _log_remove_mutation(mutation_id):
        Logger.log("Removed mutation {}".format(mutation_id), level=LogLevel.Info, log_type=LogType.GameLogic)
