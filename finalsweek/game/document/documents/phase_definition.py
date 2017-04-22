from game.document.documents.document_base import DocumentBase


class PhaseDefinition(DocumentBase):

    def __init__(self, base_data, parent=None):
        self.phase_type = None
        self.turn_sets = None
        self.automatic = None
        super().__init__(base_data, parent)

    _field_definitions = {
        "phase_type": str,
        "turn_sets":  int,
        "automatic":  bool
    }
