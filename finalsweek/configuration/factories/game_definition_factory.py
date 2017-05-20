from configuration.settings import default_game_definition


class GameDefinitionSeedFactory(object):
    @staticmethod
    def create():
        return default_game_definition
