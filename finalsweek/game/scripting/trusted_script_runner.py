from game.scripting.api.actor_api import ActorApi
from game.scripting.api.prompt_api import PromptException
from game.scripting.api.seat_api import SeatApi
from game.scripting.api.student_api import StudentApi
from game.scripting.repositories import ScriptContextRepository
from logger import log
from util.helpers import set_in_dict


class ScriptResult(object):
    def __init__(self, exports) -> None:
        super().__init__()
        self.exports = exports


class TrustedScriptRunner(object):
    @staticmethod
    def exec(script, _scope_vars):
        exec(script, _scope_vars, _scope_vars)

    def run(self, api, script):
        repository = self.build_repo(api)
        scope_vars, exports = self.build_scope(api, repository)
        self.log_script_start(api=api, scope_vars=scope_vars, exports=exports)
        try:
            self.exec(script, scope_vars)
            results = self.get_result(exports)
            self.log_script_end(api=api, results=results)
            return results
        # TODO: this shouldn't be handled in the base class
        except PromptException as e:
            self.log_script_halt()
            return self.get_result(exports, e)

    def get_result(self, exports, *a, **k):
        return ScriptResult(exports)

    def build_scope(self, api, turn_prompt, **additional_scope_vars):
        repository = self.build_repo(api)
        student_api = StudentApi(repository, api)
        actor_api = ActorApi(repository, api)
        seat_api = SeatApi(repository, api)
        scope_vars = dict(locals(), **globals())
        exports = {}
        scope_vars.update({
            "export":     lambda k, v: set_in_dict(exports, k, v),
            'StudentApi': student_api,
            'ActorApi':   actor_api,
            'SeatApi':    seat_api,
        })
        scope_vars.update(additional_scope_vars)
        return scope_vars, exports

    def build_repo(self, api):
        return ScriptContextRepository(api)

    def log_script_halt(*a, **k):
        log("Did not complete!")

    def log_script_start(*a, **k):
        log("Beginning script block:")

    def log_script_end(*a, **k):
        log("Done running script!")
