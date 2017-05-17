from game.scripting.api.program_child_api import ProgramChildApi


class CardTemplateApi(ProgramChildApi):
    def get_card_template(self, card_template_id):
        if card_template_id not in self.data.rules.card_templates:
            raise Exception("Card template not found: {}".format(card_template_id))
        return self.data.rules.card_templates.get(card_template_id)
