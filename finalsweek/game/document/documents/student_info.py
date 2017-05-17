from game.document.documents.document_base import DocumentBase


class StudentInfo(DocumentBase):
    _field_definitions = {
        "id":               str,
        "first_name":       str,
        "last_name":        str,
        "backstory":        str,
        "perk_name":        str,
        "perk_description": str,
        "fear_name":        str,
        "fear_description": str
    }

    def __init__(self, base_data, parent=None):
        self.last_name = None
        self.first_name = None
        super().__init__(base_data, parent=None)

    @property
    def display_name(self):
        return "{} {}".format(self.first_name, self.last_name)
