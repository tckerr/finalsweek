from configuration.settings import default_game_definition


class GameDefinitionFactory(object):
    @staticmethod
    def create():
        return default_game_definition
