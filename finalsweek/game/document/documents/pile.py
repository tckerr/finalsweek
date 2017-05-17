from game.document.documents.card import Card
from game.document.documents.document_base import DocumentBase


class Pile(DocumentBase):
    _field_definitions = {
        "id":    str,
        "cards": Card
    }
