from game.document.documents.document_base import DocumentBase
from game.document.documents.rules import Rules
from game.document.documents.gameflow import Gameflow
from game.document.documents.pile import Pile
from game.document.documents.seat import Seat


class Game(DocumentBase):
    _field_definitions = {
        "rules":                 Rules,
        "gameflow":              Gameflow,
        "action_card_deck":      Pile,
        "afterschool_card_deck": Pile,
        "discipline_card_deck":  Pile,
        "seats":                 Seat,
        "metadata":              dict
    }

    def __init__(self, base_data, parent=None):
        self.rules = None
        super().__init__(base_data, parent)