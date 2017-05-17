from game.document.documents.document_base import DocumentBase
from game.document.documents.operation_modifier import OperationModifier
from game.operation.mutation_matcher import MutationMatcher


class Mutation(DocumentBase):
    _field_definitions = {
        "id":                 str,
        "tags":               str,
        "priority":           int,
        "match_all":          bool,
        "gameflow_binding":   str,
        "uses":               int,
        "operation_modifier": OperationModifier,
        "targeted_actor_id":  str,
        "source_actor_id":    str
    }

    def __init__(self, base_data, parent=None):
        self.source_actor_id = None
        self.id = None
        self.gameflow_binding = None
        self.uses = None
        self.targeted_actor_id = None
        self.match_all = None
        self.tags = None
        super().__init__(base_data, parent)
        self.mutation_matcher = MutationMatcher()

    @property
    def summary(self):
        return "[Binding: {binding}, " \
               "Uses: {uses}, " \
               "TargetedActor: {targeted_actor_id}, " \
               "SourceActor: {source_actor_id}]".format(
            binding=self.gameflow_binding,
            uses=self.uses,
            targeted_actor_id=self.targeted_actor_id,
            source_actor_id=self.source_actor_id
        )

    @property
    def expired(self):
        return self.uses is not None and self.uses <= 0

    def matches(self, operation):
        return not self.expired and self.mutation_matcher.matches(self, operation)

    def decrement_uses(self):
        if self.uses is not None:
            self.uses -= 1
