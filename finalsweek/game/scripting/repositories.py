from game.operation.metadata import OperationMetadata


class ActionCardScriptContextRepository(object):
    def __init__(self, requestor_id, program_api):
        self.requestor_id = requestor_id
        self.program_api = program_api

    @property
    def metadata(self):
        metadata = OperationMetadata()
        metadata.ActionCard = True
        metadata.ActorAction = True
        metadata.Card = True
        metadata.PlayedCard = True
        return metadata

    def actors(self):
        return list(self.program_api.actors.list_actors(metadata=self.metadata))

    def students(self):
        return list(self.program_api.students.list_students(metadata=self.metadata))

    def requestor(self):
        return self.program_api.actors.get_actor(self.requestor_id, metadata=self.metadata)

    def seats(self):
        return list(self.program_api.seats.list_seats(metadata=self.metadata))
