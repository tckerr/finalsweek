from game.document.documents.document_base import DocumentBase
from game.document.documents.stage import Stage
from util import guid


class Gameflow(DocumentBase):
    _field_definitions = {
        "stages": Stage
    }

    def __init__(self, base_data, parent=None):
        self.stages = None
        super().__init__(base_data, parent)

    def add_stage(self, stage_type):
        stage_data = {
            "id":         guid(),
            "stage_type": stage_type,
            "completed":  None,
            "phases":     []
        }
        cls = self._field_definitions["stages"]
        stage = cls(stage_data, parent=self)
        self.stages.append(stage)
        return stage
