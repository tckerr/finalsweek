from game.document.documents.card import Card
from game.document.documents.document_base import DocumentBase


class InPlayEffect(DocumentBase):
    _field_definitions = {
        "id":                    str,
        "mutation_id":           str,
        "card":                  Card
    }

    def __init__(self, base_data, parent=None):
        super().__init__(base_data, parent)