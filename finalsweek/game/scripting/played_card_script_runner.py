from game.scripting.api.prompt_api import PromptApi
from game.scripting.repositories import ActionCardScriptContextRepository, PromptScriptContextRepository
from game.scripting.trusted_script_runner import TrustedScriptRunner, ScriptResult
from trace.logger import log, Logger
from trace.definitions import LogLevel, LogType


class PromptScriptResult(ScriptResult):
    def __init__(self, exports, prompt) -> None:
        super().__init__(exports)
        self.prompt = prompt
        self.complete = prompt is None


class PromptScriptRunner(TrustedScriptRunner):
    def __init__(self, actor_id, prompt) -> None:
        super().__init__()
        self.prompt = prompt
        self.actor_id = actor_id

    def build_repo(self, api):
        return PromptScriptContextRepository(api, self.actor_id)

    def build_scope(self, api, repository, **additional_scope_vars):
        prompt_api = PromptApi(self.prompt, repository, api)
        return super().build_scope(api, repository, PromptApi=prompt_api, **additional_scope_vars)

    def log_script_halt(self, *a, **k):
        log("Script did not complete! Prompt must be resolved.")

    def get_result(self, exports, exception=None, **kwargs):
        prompt = exception.prompt if exception else None
        return PromptScriptResult(exports, prompt=prompt)

    def log_script_start(self, *a, api, **k):
        super().log_script_start(self.actor_id, api, self.prompt)
        answers = {k: v["selected_option"]["id"] for k, v in self.prompt.closed.items() }
        Logger.log("Executing with answers:", answers, level=LogLevel.Info,
                   log_type=LogType.Operational)


class ActionCardScriptRunner(PromptScriptRunner):
    def build_repo(self, api):
        return ActionCardScriptContextRepository(api, self.actor_id)



