from game.document.documents.actor import Actor
from game.document.documents.document_base import DocumentBase


class Student(DocumentBase):
    _field_definitions = {
        "id":              str,
        "student_info_id": str,
        "actor":           Actor
    }

    def __init__(self, base_data, parent=None):
        self.student_info_id = None
        self.id = None
        self.actor = None
        super().__init__(base_data, parent)

    @property
    def actor_info(self):
        return self.id + " " + ("" if not self.actor else self.actor.label)

    @property
    def seat(self):
        return self._parent

    @property
    def controlled(self):
        return self.actor is not None

    @property
    def name(self):
        student_infos = self._find("Game").rules.student_infos
        for student_info in student_infos:
            if student_info.id == self.student_info_id:
                return student_info.display_name
        raise Exception("Student info not found: {}".format(self.student_info_id))
