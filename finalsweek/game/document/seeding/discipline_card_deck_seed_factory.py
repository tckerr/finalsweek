from util import guid


class DisciplineCardDeckSeedFactory(object):
    @staticmethod
    def create(cards):
        return {
            "id":    guid(),
            "cards": []
        }
