from datetime import datetime

from game.document.documents.document_base import DocumentBase
from game.document.documents.phase import Phase
from util.random import random_id


class Stage(DocumentBase):
    _field_definitions = {
        "id":         str,
        "stage_type": str,
        "completed":  datetime,
        "phases":     Phase,
    }

    def __init__(self, base_data, parent=None):
        self.phases = None
        super().__init__(base_data, parent)

    def add_phase(self, phase_type):
        phase_data = {
            "id":         random_id(),
            "phase_type": phase_type,
            "completed":  None,
            "turns":      []
        }
        cls = self._field_definitions["phases"]
        phase = cls(phase_data, parent=self)
        self.phases.append(phase)
        return phase
