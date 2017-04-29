from datetime import datetime

from game.document.documents.document_base import DocumentBase
from game.document.documents.prompt import Prompt


class Turn(DocumentBase):
    _field_definitions = {
        "id":        str,
        "actor_id":  str,
        "completed": datetime,
        "log":       list,
        "prompt":    Prompt
    }

    def __init__(self, base_data, parent=None):
        self.prompt = None
        self.completed = None
        super().__init__(base_data, parent)

    @property
    def phase(self):
        return self._parent

    def refresh(self):
        self.prompt = Prompt({
            "_id":    self.prompt._id,
            "id":     self.prompt.id,
            "closed": {},
            "open":   {}
        }, parent=self)
