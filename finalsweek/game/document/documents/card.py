from util import guid
from game.document.documents.document_base import DocumentBase


class Card(DocumentBase):
    _field_definitions = {
        "id":               str,
        "card_template_id": str
    }

    def __init__(self, base_data, parent=None):
        self.id = None
        self.card_template_id = None
        super().__init__(base_data, parent)

    @property
    def template(self):
        game = self._find("Game")
        if not game:
            raise Exception("Card has no parent game!")
        card_templates = game.rules.card_templates
        if self.card_template_id not in card_templates:
            raise Exception("Card card_template_id is not present in card template list!")
        return card_templates.get(self.card_template_id)
