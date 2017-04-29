from game.configuration.definitions import Tag


class ScriptContextRepository(object):
    def __init__(self, program_api):
        self.program_api = program_api

    @property
    def default_tags(self):
        return set()

    def actors(self):
        return list(self.program_api.actors.list_actors())

    def students(self):
        return list(self.program_api.students.list_students())

    def seats(self):
        return list(self.program_api.seats.list_seats())


class ActionCardScriptContextRepository(ScriptContextRepository):
    def __init__(self, program_api, requestor_id):
        super().__init__(program_api)
        self.requestor_id = requestor_id

    @property
    def default_tags(self):
        return {Tag.ActionCard, Tag.ActorAction, Tag.Card, Tag.PlayedCard}

    def requestor(self):
        return self.program_api.actors.get_actor(self.requestor_id)
