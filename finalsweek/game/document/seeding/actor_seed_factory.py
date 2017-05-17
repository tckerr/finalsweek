from util.random import random_id, random_name


class ActorSeedFactory(object):
    @staticmethod
    def create():
        return {
            "id":                    random_id(),
            "name":                  random_name(),
            "user_id":               None,
            "action_card_hand":      {
                "id":    random_id(),
                "cards": []
            },
            "afterschool_card_hand": {
                "id":    random_id(),
                "cards": []
            },
            "discipline_card_hand":  {
                "id":    random_id(),
                "cards": []
            },
            "cards_in_play":         [],
            "grades":                0,
            "popularity":            0,
            "torment":               0,
            "trouble":               0
        }
