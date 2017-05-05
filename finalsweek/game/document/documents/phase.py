from datetime import datetime

from game.document.documents.document_base import DocumentBase
from game.document.documents.mutation import Mutation
from game.document.documents.turn import Turn
from game.document.seeding.prompt_seed_factory import PromptSeedFactory


class Phase(DocumentBase):
    _field_definitions = {
        "id":         str,
        "phase_type": str,
        "completed":  datetime,
        "turns":      Turn,
        "mutations":  Mutation
    }

    @property
    def stage(self):
        return self._parent

    def __init__(self, base_data, parent=None):
        self.prompt_seed_factory = PromptSeedFactory()
        self.phase_type = None
        super().__init__(base_data, parent)
