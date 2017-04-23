from game.document.seeding.action_card_deck_seed_factory import ActionCardDeckSeedFactory
from game.document.seeding.afterschool_card_deck_seed_factory import AfterSchoolCardDeckSeedFactory
from game.document.seeding.card_template_seed_factory import CardTemplateSeedFactory
from game.document.seeding.discipline_card_deck_seed_factory import DisciplineCardDeckSeedFactory
from game.document.seeding.game_definition_seed_factory import GameDefinitionSeedFactory
from game.document.seeding.seat_seed_factory import SeatSeedFactory
from game.document.seeding.settings_seed_factory import SettingsSeedFactory
from game.document.seeding.student_info_seed_factory import StudentInfoSeedFactory
from game.models import Card, StudentInfo
from game.settings import default_game_definition, base_settings
from random import shuffle, choice
from util import guid
import names


class NewGameSeedFactory(object):
    def __init__(self):
        self.game_definition_seed_factory = GameDefinitionSeedFactory()
        self.settings_seed_factory = SettingsSeedFactory()
        self.card_template_seed_factory = CardTemplateSeedFactory()
        self.student_info_seed_factory = StudentInfoSeedFactory()
        self.action_card_deck_seed_factory = ActionCardDeckSeedFactory()
        self.afterschool_card_deck_seed_factory = AfterSchoolCardDeckSeedFactory()
        self.discipline_card_deck_seed_factory = DisciplineCardDeckSeedFactory()
        self.seat_seed_factory = SeatSeedFactory()




    def generate(self, player_count):
        # todo replace all the factories with these
        game_definition = self.game_definition_seed_factory.create()
        settings = self.settings_seed_factory.create()

        card_templates = self.card_template_seed_factory.create()
        student_info = self.student_info_seed_factory.create()
        action_card_deck = self.action_card_deck_seed_factory.create(card_templates, settings)
        afterschool_card_deck = self.afterschool_card_deck_seed_factory.create(card_templates)
        discipline_card_deck = self.discipline_card_deck_seed_factory.create(card_templates)
        seats = self.seat_seed_factory.create(settings, student_info, player_count)
        data = {
            "rules":                 {
                "settings":        settings,
                "card_templates":  card_templates,
                "student_infos":   student_info,
                "game_definition": game_definition
            },
            "gameflow":              {"stages": []},
            "action_card_deck":      action_card_deck,
            "afterschool_card_deck": afterschool_card_deck,
            "discipline_card_deck":  discipline_card_deck,
            "seats":                 seats,
            "metadata":              {}
        }
        return data
