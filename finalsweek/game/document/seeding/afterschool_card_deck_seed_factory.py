from util.util import guid


class AfterSchoolCardDeckSeedFactory(object):
    @staticmethod
    def create(cards):
        return {
            "id":    guid(),
            "cards": []
        }
