from game.document.documents.document_base import DocumentBase


class OperationModifier(DocumentBase):
    _field_definitions = {
        "id":     str,
        "script": str
    }
