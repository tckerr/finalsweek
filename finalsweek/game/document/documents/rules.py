from game.document.documents.card_template import CardTemplate
from game.document.documents.document_base import DocumentBase, IdDict
from game.document.documents.mutation_template import MutationTemplate
from game.document.documents.settings import Settings
from game.document.documents.stage_definition import StageDefinition
from game.document.documents.student_info import StudentInfo


class CardTemplateIdDict(IdDict):
    cls = CardTemplate


class MutationTemplateIdDict(IdDict):
    cls = MutationTemplate


class Rules(DocumentBase):
    _field_definitions = {
        "card_templates":     CardTemplateIdDict,
        "mutation_templates": MutationTemplateIdDict,
        "settings":           Settings,
        "student_infos":      StudentInfo,
        "game_definition":    StageDefinition
    }
