from game.models import Card


class CardTemplateAdapter(object):
    @staticmethod
    def adapt(data):
        return {
            "id":                   str(data.id),
            "card_type":            data.card_type_id,
            "description":          data.description,
            "script":               data.script,
            "name":                 data.name,
            "trouble_cost":         data.trouble_cost,
            "mutation_template_id": data.mutation_template_id,
        }


class CardTemplateSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.card_template_adapter = CardTemplateAdapter()

    def create(self):
        default_card_templates = list(Card.objects.filter(active=True))
        templates = {}
        for template in default_card_templates:
            adapted = self.card_template_adapter.adapt(template)
            templates[adapted["id"]] = adapted
        return templates
