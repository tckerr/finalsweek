from game.scripting.trusted_script_runner import TrustedScriptRunner
from logger import log


class MutationScriptRunnerFactory(object):
    @staticmethod
    def create(operation):
        return MutationScriptRunner(operation)


class MutationScriptRunner(TrustedScriptRunner):
    def __init__(self, operation) -> None:
        self._operation = operation

    def build_scope(self, api, repository, **additional_scope_vars):
        return super().build_scope(api, repository, operation=self._operation)

    def log_script_start(*a, scope_vars, **k):
        operation = scope_vars.get("operation")
        log("Beginning mutation script block, matched on tags:", operation.tags)
        log("   +--- Mutation value before script: {}".format(operation.value))

    def log_script_end(*a, results, **k):
        operation = results.exports.get("operation")
        log("   +--- Mutation value after script: {}".format(operation.value))
