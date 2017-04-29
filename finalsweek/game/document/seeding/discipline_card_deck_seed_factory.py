from util.random import random_id


class DisciplineCardDeckSeedFactory(object):
    @staticmethod
    def create(cards):
        return {
            "id":    random_id(),
            "cards": []
        }
