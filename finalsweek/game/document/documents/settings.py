from game.document.documents.document_base import DocumentBase


class Settings(DocumentBase):
    _field_definitions = {
        "hand_size":                  int,
        "action_card_deck_size":      int,
        "discipline_card_deck_size":  int,
        "afterschool_card_deck_size": int,
        "seat_rows":                  int,
        "seat_columns":               int,
        "total_students":             int,
        "grades_per_row":             int,
        "trouble_per_row":            int,
    }
