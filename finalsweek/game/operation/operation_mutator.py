from game.configuration.definitions import LogLevel, LogType
from game.exceptions import ExportException
from game.scripting.mutation_script_runner import MutationScriptRunnerFactory
from logger import Logger


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
        if "operation" not in result.exports:
            raise ExportException("Operation modifier scripts must export an 'operation'")
        # TODO: extract
        mutation.decrement_uses()
        self.log_mutation_details(mutation)
        if mutation.expired:
            self.program_api.actors.remove_card_in_play(mutation.id)
        return operation

    @staticmethod
    def log_mutation_details(mutation):
        message = "Mutation {} finished processing".format(mutation.summary)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
        if mutation.expired:
            Logger.log("Mutation expired ({})".format(mutation.id), level=LogLevel.Info, log_type=LogType.GameLogic)

    @staticmethod
    def _get_script(mutation):
        operation_modifier = mutation.operation_modifier
        return operation_modifier.script
