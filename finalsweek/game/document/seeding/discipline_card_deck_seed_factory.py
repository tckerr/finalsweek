from random import shuffle

from util import guid


class AfterSchoolCardDeckSeedFactory(object):
    @staticmethod
    def _afterschool_card_deck(cards):
        return {
            "id":    guid(),
            "cards": []
        }
