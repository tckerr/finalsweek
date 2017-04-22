from game.document.documents.actor import Actor
from game.document.documents.document_base import DocumentBase


class Student(DocumentBase):
    _field_definitions = {
        "id":              str,
        "student_info_id": str,
        "actor":           Actor
    }

    @property
    def seat(self):
        return self._parent

    @property
    def controlled(self):
        return self.actor is not None
