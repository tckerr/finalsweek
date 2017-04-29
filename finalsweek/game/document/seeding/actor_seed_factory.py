import names

from game.configuration.settings import generation
from util.util import guid

names.random = generation["random"]


class ActorSeedFactory(object):
    @staticmethod
    def create():
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
            "cards_in_play":         [],
            "grades":                0,
            "popularity":            0,
            "torment":               0,
            "trouble":               0
        }
