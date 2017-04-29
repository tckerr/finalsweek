from game.configuration.definitions import MutationExpiryType, GameflowMessageType
from game.document.documents.document_base import DocumentBase
from game.document.documents.operation_modifier import OperationModifier
from game.operation.mutation_matcher import MutationMatcher


class Mutation(DocumentBase):
    _field_definitions = {
        "id":                 str,
        "tags":               str,
        "priority":           int,
        "match_all":          bool,
        "expiry_criteria":    str,
        "operation_modifier": OperationModifier,
        "targeted_actor_id":  str,
        "source_actor_id":    str
    }

    def __init__(self, base_data, parent=None):
        self.id = None
        self.expiry_criteria = None
        self.targeted_actor_id = None
        self.match_all = None
        self.tags = None
        self.completed = False
        super().__init__(base_data, parent)
        self.mutation_matcher = MutationMatcher()

    @property
    def expired(self):
        return self.completed

    def matches(self, operation):
        return not self.completed and self.mutation_matcher.matches(self, operation)

    #TODO: move to different class
    def message(self, api, message):
        if message.type_completed == GameflowMessageType.Use:
            if MutationExpiryType.UseBound in self.expiry_criteria:
                self.completed = True
        elif message.type_completed == GameflowMessageType.Action:
            if MutationExpiryType.ActionBound in self.expiry_criteria \
                    and self.actor_is_me(api, message):
                self.completed = True
        elif message.type_completed == GameflowMessageType.Turn:
            if MutationExpiryType.TurnBound in self.expiry_criteria \
                    and self.actor_is_me(api, message):
                self.completed = True
        elif message.type_completed == GameflowMessageType.Phase:
            if MutationExpiryType.PhaseBound in self.expiry_criteria:
                self.completed = True
        elif message.type_completed == GameflowMessageType.Stage:
            if MutationExpiryType.StageBound in self.expiry_criteria:
                self.completed = True
        if self.completed:
            api.actors.remove_mutation_and_card_in_play(self.id)

    def actor_is_me(self, api, message):
        if message.actor_id:
            actor = api.actors.get_by_mutation(self.id)
            if actor and actor.id == message.actor_id:
                return True
        return False
