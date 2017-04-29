from game.scripting.api.prompt_api import PromptApi
from game.scripting.repositories import ActionCardScriptContextRepository
from game.scripting.trusted_script_runner import TrustedScriptRunner, ScriptResult
from logger import log


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
        log("   +--- Did not complete! Prompt must be resolved.")

    def get_result(self, exports, exception=None, **kwargs):
        prompt = exception.prompt if exception else None
        return ActionCardScriptResult(exports, prompt=prompt)

    def log_script_start(self, *a, api, **k):
        super().log_script_start(self.actor_id, api, self.turn_prompt)
        actor = api.actors.get_actor(self.actor_id)
        log("   +--- Prior to running script, requester:", actor.name, self.actor_id)
        for actor in api.actors.list_actors():
            log("   +------ {}: {}".format(actor.id, actor.summary))
        log("   +--- Executing with answers:", self.turn_prompt.closed)

    @staticmethod
    def log_script_end(api, *a, **k):
        log("   +--- After running script:")
        for actor in api.actors.list_actors():
            log("   +------ {}: {}".format(actor.id, actor.summary))
