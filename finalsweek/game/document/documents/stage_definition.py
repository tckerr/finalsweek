from game.document.documents.document_base import DocumentBase
from game.document.documents.phase_definition import PhaseDefinition


class StageDefinition(DocumentBase):
    _field_definitions = {
        "stage_type": str,
        "phase_sets": int,
        "phases":     PhaseDefinition
    }
