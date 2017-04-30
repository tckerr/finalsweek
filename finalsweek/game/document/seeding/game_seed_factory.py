from game.document.seeding.action_card_deck_seed_factory import ActionCardDeckSeedFactory
from game.document.seeding.afterschool_card_deck_seed_factory import AfterSchoolCardDeckSeedFactory
from game.document.seeding.discipline_card_deck_seed_factory import DisciplineCardDeckSeedFactory
from game.document.seeding.rules_seed_factory import RulesSeedFactory
from game.document.seeding.seat_seed_factory import SeatSeedFactory


class GameSeedFactory(object):
    def __init__(self):
        self.rules_seed_factory = RulesSeedFactory()
        self.action_card_deck_seed_factory = ActionCardDeckSeedFactory()
        self.afterschool_card_deck_seed_factory = AfterSchoolCardDeckSeedFactory()
        self.discipline_card_deck_seed_factory = DisciplineCardDeckSeedFactory()
        self.seat_seed_factory = SeatSeedFactory()

    def generate(self, player_count):
        # todo replace all the factories with these
        rules = self.rules_seed_factory.create()
        action_card_deck = self.action_card_deck_seed_factory.create(rules["card_templates"], rules["settings"])
        afterschool_card_deck = self.afterschool_card_deck_seed_factory.create(rules["card_templates"])
        discipline_card_deck = self.discipline_card_deck_seed_factory.create(rules["card_templates"])
        seats = self.seat_seed_factory.create(rules["settings"], rules["student_infos"], player_count)
        data = {
            "rules":                  rules,
            "gameflow":               {"stages": []},
            "action_card_deck":       action_card_deck,
            "afterschool_card_deck":  afterschool_card_deck,
            "discipline_card_deck":   discipline_card_deck,
            "phase_discipline_cards": {},
            "seats":                  seats,
            "mutations":              [],
            "metadata":               {}
        }
        return data
