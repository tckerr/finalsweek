class ScriptContextRepository(object):
    def __init__(self, requestor_id, program_api):
        self.requestor_id = requestor_id
        self.program_api = program_api

    def actors(self):
        return list(self.program_api.actors.list_actors())

    def students(self):
        return list(self.program_api.students.list_students())

    def requestor(self):
        return self.program_api.actors.get_actor(self.requestor_id)

    def seats(self):
        return list(self.program_api.seats.list_seats())
