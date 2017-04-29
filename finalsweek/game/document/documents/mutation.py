from game.document.documents.document_base import DocumentBase
from game.document.documents.operation_modifier import OperationModifier
from game.operation.mutation_matcher import MutationMatcher
from game.operation.mutation_message_receiver import MutationMessageReceiver


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
        self.mutation_message_receiver = MutationMessageReceiver()

    @property
    def expired(self):
        return self.completed

    def matches(self, operation):
        return not self.completed and self.mutation_matcher.matches(self, operation)
