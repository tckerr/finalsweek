from util.random import random_id


class AfterSchoolCardDeckSeedFactory(object):
    @staticmethod
    def create(cards):
        return {
            "id":    random_id(),
            "cards": []
        }
