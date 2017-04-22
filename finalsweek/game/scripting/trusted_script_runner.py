from game.scripting.api.actor_api import ActorApi
from game.scripting.api.prompt_api import PromptApi, PromptException
from game.scripting.api.seat_api import SeatApi
from game.scripting.api.student_api import StudentApi
from game.scripting.repositories import ScriptContextRepository


class TrustedScriptRunner(object):
    def __init__(self):
        pass

    @staticmethod
    def run(actor_id, api, script, turn_prompt):
        actor = api.actors.get_actor(actor_id)
        print("Beginning script block:")
        print("   +--- Prior to running script, requester:", actor.name, actor_id)
        for actor in api.actors.list_actors():
            print("   +------ {}: {}".format(actor.id, actor.summary))
        print("   +--- Executing with answers:", turn_prompt.closed)
        repository = ScriptContextRepository(actor_id, api)
        student_api = StudentApi(repository, api)
        actor_api = ActorApi(repository, api)
        seat_api = SeatApi(repository, api)
        prompt_api = PromptApi(turn_prompt, repository, api)
        scope_vars = dict(locals(), **globals())
        scope_vars.update({
            'StudentApi':  student_api,
            'ActorApi':    actor_api,
            'SeatApi':     seat_api,
            'PromptApi':   prompt_api
        })

        try:
            exec(script, scope_vars, scope_vars)
            print("   +--- After running script:")
            for actor in api.actors.list_actors():
                print("   +------ {}: {}".format(actor.id, actor.summary))

        except PromptException as e:
            print("   +--- Did not complete! Prompt must be resolved.")
            return e.prompt
