from game.exceptions import ExportException
from game.scripting.mutation_script_runner import MutationScriptRunnerFactory


class OperationMutator(object):
    def __init__(self, program_api) -> None:
        super().__init__()
        self.program_api = program_api
        self.mutation_script_runner_factory = MutationScriptRunnerFactory()

    def mutate(self, operation, mutations):
        for mutation in mutations:
            operation = self._mutate_single(mutation, operation)
        return operation

    def _mutate_single(self, mutation, operation):
        if not mutation.matches(operation):
            return operation
        script = self._get_script(mutation)
        runner = self.mutation_script_runner_factory.create(operation)
        result = runner.run(self.program_api, script)
        self.decrement_and_expire_mutation(mutation)
        if "operation" not in result.exports:
            raise ExportException("Operation modifier scripts must export an 'operation'")
        return operation

    def decrement_and_expire_mutation(self, mutation):
        mutation.decrement_uses()
        if mutation.expired:
            self.program_api.actors.remove_mutation_and_card_in_play(mutation.id)

    @staticmethod
    def _get_script(mutation):
        operation_modifier = mutation.operation_modifier
        return operation_modifier.script