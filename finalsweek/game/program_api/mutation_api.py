from game.operation.factories import MutationFactory
from game.operation.operation_mutator import OperationMutator
from game.scripting.api.program_child_api import ProgramChildApi


class MutationApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.mutation_factory = MutationFactory()
        self.operation_mutator = OperationMutator(program_api)

    def create_and_register(self, mutation_template, **exports):
        mutation = self.mutation_factory.create_from_template(mutation_template, **exports)
        self.data.mutations.append(mutation)
        self._sort_mutations()
        return mutation

    def mutate(self, operation):
        return self.operation_mutator.mutate(operation, self.data.mutations)

    def _sort_mutations(self):
        self.data.mutations = sorted(self.data.mutations, key=lambda m: m.priority)
