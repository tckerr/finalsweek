from game.document.documents.document_base import DocumentBase
from game.document.documents.operation_modifier import OperationModifier


class MutationTemplate(DocumentBase):
    _field_definitions = {
        "id":                 str,
        "tags":               str,
        "priority":           int,
        "match_all":          bool,
        "expiry_criteria":    str,
        "operation_modifier": OperationModifier,
        "uses":               int,
    }
