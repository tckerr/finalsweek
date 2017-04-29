from game.document.documents.document_base import DocumentBase
from game.document.documents.operation_modifier import OperationModifier
from util import floor_at_zero


class Mutation(DocumentBase):
    _field_definitions = {
        "id":                 str,
        "tags":               str,
        "priority":           int,
        "match_all":          bool,
        "expiry_criteria":    str,
        "operation_modifier": OperationModifier,
        "targeted_actor_id":  str,
        "source_actor_id":    str,
        "uses":               int
    }

    def __init__(self, base_data, parent=None):
        self.targeted_actor_id = None
        self.match_all = None
        self.tags = None
        self.uses = None
        super().__init__(base_data, parent)

    @property
    def expired(self):
        return self.uses == 0

    def decrement_uses(self):
        if self.uses is not None:
            self.uses = floor_at_zero(self.uses - 1)

    def matches(self, operation):
        if not self._matches_on_targeted_actor(operation):
            return False
        if self.match_all:
            return self._all_match(operation)
        return self._any_matches(operation)

    def _matches_on_targeted_actor(self, operation):
        return self.targeted_actor_id is None \
               or operation.targeted_actor_id == self.targeted_actor_id

    def _any_matches(self, operation):
        for tag in self.tags:
            if tag in operation.tags:
                return True
        return False

    def _all_match(self, operation):
        for tag in self.tags:
            if tag not in operation.tags:
                return False
        return True
