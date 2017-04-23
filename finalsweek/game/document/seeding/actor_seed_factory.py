import names

from util import guid


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
            "grades":                0,
            "popularity":            0,
            "torment":               0,
            "trouble":               0
        }
