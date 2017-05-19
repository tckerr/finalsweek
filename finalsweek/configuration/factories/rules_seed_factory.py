from configuration.factories.card_template_seed_factory import CardTemplateSeedFactory
from configuration.factories.game_definition_seed_factory import GameDefinitionSeedFactory
from configuration.factories.mutation_template_seed_factory import MutationTemplateSeedFactory
from configuration.factories.settings_seed_factory import SettingsSeedFactory
from configuration.factories.student_info_seed_factory import StudentInfoSeedFactory


class RulesSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.settings_seed_factory = SettingsSeedFactory()
        self.card_template_seed_factory = CardTemplateSeedFactory()
        self.mutation_template_seed_factory = MutationTemplateSeedFactory()
        self.student_info_seed_factory = StudentInfoSeedFactory()
        self.game_definition_seed_factory = GameDefinitionSeedFactory()

    def create(self):
        return {
            "settings":           self.settings_seed_factory.create(),
            "card_templates":     self.card_template_seed_factory.create(),
            "mutation_templates": self.mutation_template_seed_factory.create(),
            "student_infos":      self.student_info_seed_factory.create(),
            "game_definition":    self.game_definition_seed_factory.create()
        }
