from game.models import Card, StudentInfo
from game.settings import default_game_definition
from random import shuffle, choice
from util import guid
import names


class CardTemplateAdapter(object):
    @staticmethod
    def adapt(data):
        return {
            "id":           str(data.id),
            "card_type":    data.card_type_id,
            "description":  data.description,
            "script":       data.script,
            "name":         data.name,
            "trouble_cost": data.trouble_cost
        }


class StudentInfoAdapter(object):
    @staticmethod
    def adapt(data):
        return {
            "id":               str(data.id),
            "first_name":       data.first_name,
            "last_name":        data.last_name,
            "backstory":        data.backstory,
            "perk_name":        data.perk_name,
            "perk_description": data.perk_description,
            "fear_name":        data.fear_name,
            "fear_description": data.fear_description
        }


class GameSeedGenerator(object):
    def __init__(self):
        self.card_template_adapter = CardTemplateAdapter()
        self.student_info_adapter = StudentInfoAdapter()
        self.total_cards = 1000

    @staticmethod
    def _settings():
        return {
            "hand_size":      6,
            "total_cards":    1000,
            "seat_rows":      5,
            "seat_columns":   4,
            "total_students": 16
        }

    def _card_templates(self):
        default_card_templates = list(Card.objects.filter(active=True))
        templates = {}
        for template in default_card_templates:
            adapted = self.card_template_adapter.adapt(template)
            templates[adapted["id"]] = adapted
        return templates

    def _student_infos(self):
        default_student_infos = list(StudentInfo.objects.all())
        return [self.student_info_adapter.adapt(card) for card in default_student_infos]

    def _action_card_deck(self, templates):
        template_list = templates.values()
        filtered_templates = list(filter(lambda c: c["card_type"] == "Action", template_list))
        cards_per_type = int(self.total_cards / len(filtered_templates))
        card_list = []
        for template in filtered_templates:
            for _ in range(0, cards_per_type):
                card_list.append({
                    "id":                       guid(),
                    "card_template_id": template["id"]
                })
        shuffle(card_list)
        return {
            "id":    guid(),
            "cards": card_list
        }

    @staticmethod
    def _afterschool_card_deck(cards):
        return {
            "id":    guid(),
            "cards": []
        }

    @staticmethod
    def _discipline_card_deck(cards):
        return {
            "id":    guid(),
            "cards": []
        }

    def _seats(self, settings, student_infos, player_count):
        seats = []
        total = settings["total_students"]
        for row in range(0, settings["seat_rows"]):
            for column in range(0, settings["seat_columns"]):
                seat = {
                    "id":      guid(),
                    "row":     row,
                    "column":  column,
                    "student": None
                }
                if total > 0:
                    seat["student"] = self._student(student_infos, player_count > 0)
                    total -= 1
                    player_count -= 1
                seats.append(seat)
        return seats

    def _student(self, student_infos, as_actor=False):
        student_info_id = choice(student_infos)["id"]
        actor = self._actor() if as_actor else None
        return {
            "id":              guid(),
            "student_info_id": student_info_id,
            "actor":           actor
        }

    def _actor(self, ):
        return {
            "id":                    guid(),
            "name":                  names.get_full_name(),
            "user_id":               None,
            "action_card_hand":      {
                "id":    guid(),
                "cards": []
            },
            "afterschool_card_hand": {
                "id":    guid(),
                "cards": []
            },
            "discipline_card_hand":  {
                "id":    guid(),
                "cards": []
            },
            "grades":                0,
            "popularity":            0,
            "torment":               0,
            "trouble":               0
        }

    def generate(self, player_count):
        # todo replace all the factories with these
        game_definition = default_game_definition
        settings = self._settings()
        card_templates = self._card_templates()
        student_infos = self._student_infos()
        action_card_deck = self._action_card_deck(card_templates)
        afterschool_card_deck = self._afterschool_card_deck(card_templates)
        discipline_card_deck = self._discipline_card_deck(card_templates)
        seats = self._seats(settings, student_infos, player_count)
        data = {
            "rules":                 {
                "settings":        settings,
                "card_templates":  card_templates,
                "student_infos":   student_infos,
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
