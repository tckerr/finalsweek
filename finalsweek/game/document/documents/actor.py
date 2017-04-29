from game.document.documents.in_play_effect import InPlayEffect
from game.document.documents.document_base import DocumentBase
from game.document.documents.pile import Pile


class Actor(DocumentBase):
    _field_definitions = {
        "id":                    str,
        "user_id":               str,
        "name":                  str,
        "action_card_hand":      Pile,
        "afterschool_card_hand": Pile,
        "discipline_card_hand":  Pile,
        "cards_in_play":         InPlayEffect,
        "grades":                int,
        "popularity":            int,
        "torment":               int,
        "trouble":               int
    }

    def __init__(self, base_data, parent=None):
        self.name = None
        self.id = None
        self.torment = None
        self.trouble = None
        self.popularity = None
        self.grades = None
        super().__init__(base_data, parent)

    @property
    def student(self):
        return self._parent

    @property
    def seat(self):
        seat = self.student.seat
        if seat is None:
            raise Exception("Student {} seat is empty.".format(self.id))
        return seat

    @property
    def label(self):
        return "{} ({})".format(self.name, self.id)

    @property
    def summary(self):
        return "[ Name: {name}, " \
               "Grades: {grades}, " \
               "Pop: {popularity}, " \
               "Trouble: {trouble}, " \
               "Tor: {torment}, " \
               "Student ({student_id}) Seat: {coordinates}]" \
            .format(
            name=self.name,
            grades=self.grades,
            popularity=self.popularity,
            trouble=self.trouble,
            torment=self.torment,
            student_id=self.student.id,
            coordinates=self.student.seat.coordinates_str)
