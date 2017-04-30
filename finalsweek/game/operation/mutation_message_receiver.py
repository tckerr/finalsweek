from game.configuration.definitions import GameflowMessageType, MutationExpiryType


class MutationMessageReceiver(object):
    def message(self, api, message, mutation):
        if message.type_completed == GameflowMessageType.Use:
            if MutationExpiryType.UseBound in mutation.expiry_criteria:
                mutation.completed = True
        elif message.type_completed == GameflowMessageType.Action:
            if MutationExpiryType.ActionBound in mutation.expiry_criteria \
                    and self.actor_match(api, message, mutation):
                mutation.completed = True
        elif message.type_completed == GameflowMessageType.Turn:
            if MutationExpiryType.TurnBound in mutation.expiry_criteria \
                    and self.actor_match(api, message, mutation):
                mutation.completed = True
        elif message.type_completed == GameflowMessageType.Phase:
            if MutationExpiryType.PhaseBound in mutation.expiry_criteria:
                mutation.completed = True
        elif message.type_completed == GameflowMessageType.Stage:
            if MutationExpiryType.StageBound in mutation.expiry_criteria:
                mutation.completed = True
        if mutation.completed:
            api.actors.remove_mutation_and_card_in_play(mutation.id)

    @staticmethod
    def actor_match(api, message, mutation):
        if message.actor_id:
            actor = api.actors.get_by_mutation(mutation.id)
            if actor and actor.id == message.actor_id:
                return True
        return False
