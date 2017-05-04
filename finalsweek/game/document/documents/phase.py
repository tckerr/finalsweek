from datetime import datetime

from game.document.documents.document_base import DocumentBase
from game.document.documents.mutation import Mutation
from game.document.documents.prompt import Prompt
from game.document.documents.turn import Turn
from util.random import random_id


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
        self.phase_type = None
        super().__init__(base_data, parent)

    def create_turn(self, actor_id):
        turn_data = {
            "id":        random_id(),
            "actor_id":  actor_id,
            "log":       [],
            "completed": None,
            "prompt":    self.create_prompt(),
            "mutations":  []
        }
        cls = self._field_definitions["turns"]
        turn = cls(turn_data, parent=self)
        self.turns.append(turn)
        return turn

    @staticmethod
    def create_prompt():
        return Prompt({
            "id":     random_id(),
            "open":   {},
            "closed": {}
        })
