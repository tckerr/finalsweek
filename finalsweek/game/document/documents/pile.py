from game.document.documents.document_base import DocumentBase
from game.document.documents.card import Card


class Pile(DocumentBase):
    _field_definitions = {
        "id":    str,
        "cards": Card
    }
