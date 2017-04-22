from game.document.documents.document_base import DocumentBase


class CardTemplate(DocumentBase):
    _field_definitions = {
        "id":           str,
        "card_type":    str,
        "description":  str,
        "script":       str,
        "name":         str,
        "trouble_cost": int
    }
