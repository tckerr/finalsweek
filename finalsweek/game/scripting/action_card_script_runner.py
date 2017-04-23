from game.scripting.api.actor_api import ActorApi
from game.scripting.api.prompt_api import PromptException, PromptApi
from game.scripting.api.seat_api import SeatApi
from game.scripting.api.student_api import StudentApi
from game.scripting.repositories import ActionCardScriptContextRepository
from game.scripting.trusted_script_runner import TrustedScriptRunner


class ActionCardScriptRunner(TrustedScriptRunner):
    def __init__(self):
        pass

    def run(self, actor_id, api, script, turn_prompt):

        scope_vars = self.build_scope(actor_id, api, turn_prompt)
        self.log_script_start(actor_id, api, turn_prompt)
        try:
            self.exec(script, scope_vars, scope_vars)
            self.log_script_end(api)
        except PromptException as e:
            self.log_script_halt()
            return e.prompt

    @staticmethod
    def build_scope(actor_id, api, turn_prompt):
        repository = ActionCardScriptContextRepository(actor_id, api)
        student_api = StudentApi(repository, api)
        actor_api = ActorApi(repository, api)
        seat_api = SeatApi(repository, api)
        prompt_api = PromptApi(turn_prompt, repository, api)
        scope_vars = dict(locals(), **globals())
        scope_vars.update({
            'StudentApi': student_api,
            'ActorApi':   actor_api,
            'SeatApi':    seat_api,
            'PromptApi':  prompt_api
        })
        return scope_vars

    @staticmethod
    def log_script_halt():
        print("   +--- Did not complete! Prompt must be resolved.")

    @staticmethod
    def log_script_start(actor_id, api, turn_prompt):
        actor = api.actors.get_actor(actor_id)
        print("Beginning script block:")
        print("   +--- Prior to running script, requester:", actor.name, actor_id)
        for actor in api.actors.list_actors():
            print("   +------ {}: {}".format(actor.id, actor.summary))
        print("   +--- Executing with answers:", turn_prompt.closed)

    @staticmethod
    def log_script_end(api):
        print("   +--- After running script:")
        for actor in api.actors.list_actors():
            print("   +------ {}: {}".format(actor.id, actor.summary))
