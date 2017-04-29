from game.document.seeding.card_template_seed_factory import CardTemplateSeedFactory
from game.document.seeding.game_definition_seed_factory import GameDefinitionSeedFactory
from game.document.seeding.mutation_template_seed_factory import MutationTemplateSeedFactory
from game.document.seeding.settings_seed_factory import SettingsSeedFactory
from game.document.seeding.student_info_seed_factory import StudentInfoSeedFactory


class RulesSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.settings_seed_factory = SettingsSeedFactory()
        self.card_template_seed_factory = CardTemplateSeedFactory()
        self.mutation_template_seed_factory = MutationTemplateSeedFactory()
        self.student_info_seed_factory = StudentInfoSeedFactory()
        self.game_definition_seed_factory = GameDefinitionSeedFactory()

    def create(self):
        settings = self.settings_seed_factory.create()
        card_templates = self.card_template_seed_factory.create()
        mutation_templates = self.mutation_template_seed_factory.create()
        student_info = self.student_info_seed_factory.create()
        game_definition = self.game_definition_seed_factory.create()
        return {
            "settings":             settings,
            "card_templates":       card_templates,
            "mutation_templates":   mutation_templates,
            "student_infos":        student_info,
            "game_definition":      game_definition
        }
