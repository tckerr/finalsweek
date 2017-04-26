from game.document.documents.mutation import Mutation
from game.document.documents.operation_metadata import OperationMetadata
from game.scripting.api.program_child_api import ProgramChildApi
from util import guid


class MutationApi(ProgramChildApi):

    def register(self, priority=0, **kwargs):
        criteria = OperationMetadata.default_data()
        criteria.update(kwargs)
        mutation_data = {
            "id": guid(),
            "priority": priority,
            "criteria": criteria
        }
        self.data.mutations.append(Mutation(mutation_data))
        self.data.mutations = sorted(self.data.mutations, key=lambda m: m.priority)

    def mutate(self, operation):
        for mutation in self.data.mutations:
            operation = mutation.mutate_on_match(operation)
        return operation
