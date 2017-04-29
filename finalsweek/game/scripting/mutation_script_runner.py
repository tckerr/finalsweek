from game.scripting.trusted_script_runner import TrustedScriptRunner


class MutationScriptRunnerFactory(object):
    def create(self, operation):
        return MutationScriptRunner(operation)


class MutationScriptRunner(TrustedScriptRunner):
    def __init__(self, operation) -> None:
        self._operation = operation

    def build_scope(self, api, repository, **additional_scope_vars):
        return super().build_scope(api, repository, operation=self._operation)
