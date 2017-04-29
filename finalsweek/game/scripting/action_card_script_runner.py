from game.configuration.definitions import LogLevel, LogType
from game.scripting.api.prompt_api import PromptApi
from game.scripting.repositories import ActionCardScriptContextRepository
from game.scripting.trusted_script_runner import TrustedScriptRunner, ScriptResult
from logger import log, Logger


class ActionCardScriptResult(ScriptResult):
    def __init__(self, exports, prompt) -> None:
        super().__init__(exports)
        self.prompt = prompt
        self.complete = prompt is None


class ActionCardScriptRunner(TrustedScriptRunner):
    def __init__(self, actor_id, turn_prompt) -> None:
        super().__init__()
        self.turn_prompt = turn_prompt
        self.actor_id = actor_id

    def build_repo(self, api):
        return ActionCardScriptContextRepository(api, self.actor_id)

    def build_scope(self, api, repository, **additional_scope_vars):
        prompt_api = PromptApi(self.turn_prompt, repository, api)
        return super().build_scope(api, repository, PromptApi=prompt_api, **additional_scope_vars)

    def log_script_halt(self, *a, **k):
        log("Script did not complete! Prompt must be resolved.")

    def get_result(self, exports, exception=None, **kwargs):
        prompt = exception.prompt if exception else None
        return ActionCardScriptResult(exports, prompt=prompt)

    def log_script_start(self, *a, api, **k):
        super().log_script_start(self.actor_id, api, self.turn_prompt)
        Logger.log("Executing with answers:", self.turn_prompt.closed, level=LogLevel.Info, log_type=LogType.Operational)

