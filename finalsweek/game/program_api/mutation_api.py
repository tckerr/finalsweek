from game.definitions import MutationGameflowBinding
from game.document.seeding.mutation_queue_seed_factory import MutationQueueFactory
from game.operation.factories import MutationFactory
from game.operation.operation_mutator import OperationMutator
from game.scripting.api.program_child_api import ProgramChildApi
from trace.definitions import LogLevel, LogType
from trace.logger import Logger


class MutationApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.mutation_factory = MutationFactory()
        self.operation_mutator = OperationMutator(program_api)
        self.mutation_queue_factory = MutationQueueFactory()

    @property
    def _mutations(self):
        turn = self.program_api.turns.get_current_turn()
        if not turn:
            return self._sorted_mutations(self.data.mutations)
        return self._sorted_mutations(turn.mutations) + \
               self._sorted_mutations(turn.phase.mutations) + \
               self._sorted_mutations(turn.phase.stage.mutations) + \
               self._sorted_mutations(self.data.mutations)

    def remove_mutation(self, mutation_id):
        new_mutations = [m for m in self.data.mutations if m.id != mutation_id]
        assert (len(new_mutations) == len(self.data.mutations) - 1)
        self._log_remove_mutation(mutation_id)
        self.data.mutations = new_mutations

    # TODO: support for lower lvl mutations
    def create_and_register(self, mutation_template, **exports):
        mutation = self.mutation_factory.create_from_template(mutation_template, **exports)
        self._register(mutation)
        message = "Creating mutation {}".format(mutation.id)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
        return mutation

    def _register(self, mutation):
        gameflow_binding = mutation.gameflow_binding
        if gameflow_binding not in [v for k, v in MutationGameflowBinding.prop_list()]:
            raise Exception("Invalid MutationGameflowBinding: {}".format(gameflow_binding))
        # TODO: convert these to "Current..." to make it clear
        if gameflow_binding == MutationGameflowBinding.Turn:
            self.program_api.turns.get_current_turn().mutations.append(mutation)
        elif gameflow_binding == MutationGameflowBinding.Phase:
            self.program_api.turns.get_current_turn().phase.mutations.append(mutation)
        elif gameflow_binding == MutationGameflowBinding.Stage:
            self.program_api.turns.get_current_turn().phase.stage.mutations.append(mutation)
        elif gameflow_binding == MutationGameflowBinding.Game:
            self.data.mutations.append(mutation)
        else:
            # register for next instance of that type
            if gameflow_binding not in self.data.mutation_queue:
                self.data.mutation_queue[gameflow_binding] = self.mutation_queue_factory.create()
            self.data.mutation_queue[gameflow_binding].mutations.append(mutation)

    def mutate(self, operation):
        return self.operation_mutator.mutate(operation, self._mutations)

    @staticmethod
    def _sorted_mutations(mutations):
        return sorted(mutations, key=lambda m: m.priority, reverse=True)

    @staticmethod
    def _log_remove_mutation(mutation_id):
        Logger.log("Removed mutation {}".format(mutation_id), level=LogLevel.Info, log_type=LogType.GameLogic)
