from game.document.documents.document_base import DocumentBase
from game.document.documents.student import Student


class Seat(DocumentBase):
    _field_definitions = {
        "id":      str,
        "row":     int,
        "column":  int,
        "student": Student
    }

    def __init__(self, base_data, parent=None):
        self.row = None
        self.column = None
        self.student = None
        super().__init__(base_data, parent)

    @property
    def actor(self):
        return self.student.actor if self.student else None

    @property
    def empty(self):
        return self.student is None

    @property
    def coordinates_str(self):
        return "({}, {})".format(self.column, self.row)
