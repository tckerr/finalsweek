from game.operation.mutation_message_receiver import MutationMessageReceiver
from game.scripting.api.program_child_api import ProgramChildApi


class GameflowMessage(object):
    def __init__(self, type_completed, actor_id=None) -> None:
        super().__init__()
        self.type_completed = type_completed
        self.actor_id = actor_id


class MessageApi(ProgramChildApi):
    def __init__(self, program_api):
        super().__init__(program_api)
        self.mutation_message_receiver = MutationMessageReceiver()

    def dispatch(self, message, mutation_id=None, exclude=None):
        for mutation in self.data.mutations:
            if mutation_id and mutation.id != mutation_id:
                continue
            # TODO: kind of a hack
            if exclude and mutation.id in exclude:
                continue
            self.mutation_message_receiver.message(self.program_api, message, mutation)