from game.document.documents.document_base import DocumentBase


class CardTemplate(DocumentBase):
    _field_definitions = {
        "id":                   str,
        "card_type":            str,
        "description":          str,
        "script":               str,
        "name":                 str,
        "trouble_cost":         int,
        "mutation_template_id": str
    }

    def __init__(self, base_data, parent=None):
        self.mutation_template_id = None
        super().__init__(base_data, parent)

    @property
    def mutation_template(self):
        game = self._find("Game")
        if not game:
            raise Exception("CardTemplate has no parent game!")
        mutation_templates = game.rules.mutation_templates
        if self.mutation_template_id not in mutation_templates:
            raise Exception("CardTemplate mutation_template_id is not present in mutation template list!")
        return mutation_templates.get(self.mutation_template_id)
