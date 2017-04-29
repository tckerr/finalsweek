from datetime import datetime

from game.document.documents.document_base import DocumentBase
from game.document.documents.prompt import Prompt
from game.document.documents.turn import Turn
from util.util import guid


class Phase(DocumentBase):
    _field_definitions = {
        "id":         str,
        "phase_type": str,
        "completed":  datetime,
        "turns":      Turn
    }

    @property
    def stage(self):
        return self._parent

    def create_turn(self, actor_id):
        turn_data = {
            "id":        guid(),
            "actor_id":  actor_id,
            "log":       [],
            "completed": None,
            "prompt":    self.create_prompt()
        }
        cls = self._field_definitions["turns"]
        turn = cls(turn_data, parent=self)
        self.turns.append(turn)
        return turn

    @staticmethod
    def create_prompt():
        return Prompt({
            "id":     guid(),
            "open":   {},
            "closed": {}
        })
