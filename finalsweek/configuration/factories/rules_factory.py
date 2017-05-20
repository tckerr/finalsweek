from configuration.factories.card_template_factory import CardTemplateFactory
from configuration.factories.game_definition_factory import GameDefinitionFactory
from configuration.factories.mutation_template_factory import MutationTemplateFactory
from configuration.factories.settings_factory import SettingsFactory
from configuration.factories.student_info_factory import StudentInfoFactory


class RulesFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.settings_factory = SettingsFactory()
        self.card_template_factory = CardTemplateFactory()
        self.mutation_template_factory = MutationTemplateFactory()
        self.student_info_factory = StudentInfoFactory()
        self.game_definition_factory = GameDefinitionFactory()

    def create(self):
        return {
            "settings":           self.settings_factory.create(),
            "card_templates":     self.card_template_factory.create(),
            "mutation_templates": self.mutation_template_factory.create(),
            "student_infos":      self.student_info_factory.create(),
            "game_definition":    self.game_definition_factory.create()
        }
