from game.document.documents.document_base import DocumentBase, IdDict
from game.document.documents.settings import Settings
from game.document.documents.student_info import StudentInfo
from game.document.documents.stage_definition import StageDefinition
from game.document.documents.card_template import CardTemplate

class CardTemplateIdDict(IdDict):
    cls = CardTemplate

class Rules(DocumentBase):
    _field_definitions = {
        "card_templates": CardTemplateIdDict,
        "settings": Settings,
        "student_infos": StudentInfo,
        "game_definition": StageDefinition
    }
