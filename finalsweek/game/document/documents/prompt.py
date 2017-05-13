from game.document.documents.document_base import DocumentBase


class Prompt(DocumentBase):
    _field_definitions = {
        "id":     str,
        "open":   dict,
        "closed": dict
    }

    def __init__(self, base_data, parent=None):
        self._id = None
        self.open = None
        self.closed = None
        super().__init__(base_data, parent)

    @property
    def is_new(self):
        return len(self.closed) == 0
