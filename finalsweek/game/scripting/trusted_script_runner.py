from django.db import transaction, models
from game.models import Actor, Student
from game.scripting.repositories import ScriptContextRepository
from game.scripting.api.student_api import StudentApi
from game.scripting.api.seat_api import SeatApi
from game.scripting.api.actor_api import ActorApi
from game.scripting.api.prompt_api import PromptApi, PromptException

class SaveQueue(list):
    def append(self, item):
        if item not in self:
            return super(SaveQueue, self).append(item)


class TrustedScriptRunner(object):

    def __init__(self):
        pass

    def run(self, actor, script, answers):

        print("        Prior to running script, requestor:", actor, actor.summary)
        print("        Executing with answers:", answers)
        save_queue = SaveQueue()
        repository = ScriptContextRepository(actor)
        student_api = StudentApi(save_queue, repository)
        actor_api = ActorApi(save_queue, repository)
        seat_api = SeatApi(save_queue, repository)
        prompt_api = PromptApi(answers, save_queue, repository)
        scope_vars = dict(locals(), **globals())
        scope_vars.update({
            '__answers__': answers,
            'StudentApi': student_api,
            'ActorApi': actor_api,
            'SeatApi': seat_api,
            'PromptApi': prompt_api
        })

        try:
            exec(script, scope_vars, scope_vars)
        except PromptException as e:
            return self.__save_and_prompt(save_queue, e.prompt)

        return self.__save(save_queue)


    def __save(self, save_queue):
        with transaction.atomic():
            for item in save_queue:
                if issubclass(item.__class__, models.Model):
                    if item.__class__ is Actor:
                        print("        * Saving changes:", item, item.summary)
                    elif item.__class__ is Student and item.actor_or_none is not None:
                        print("        * Saving changes:", item, item.actor.summary)
                    else:
                        print("        * Saving changes:", item)
                    item.save()


    def __save_and_prompt(self, save_queue, prompt):
        self.__save(save_queue)
        return prompt

