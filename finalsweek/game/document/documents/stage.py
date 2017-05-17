from datetime import datetime

from game.document.documents.document_base import DocumentBase
from game.document.documents.mutation import Mutation
from game.document.documents.phase import Phase
from game.document.seeding.phase_seed_factory import PhaseSeedFactory
from util.random import random_id


class Stage(DocumentBase):
    _field_definitions = {
        "id":         str,
        "stage_type": str,
        "completed":  datetime,
        "phases":     Phase,
        "mutations":  Mutation
    }

    def __init__(self, base_data, parent=None):
        self.phases = None
        super().__init__(base_data, parent)

