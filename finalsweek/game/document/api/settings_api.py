from game.scripting.api.base import ProgramChildApi


class SettingsApi(ProgramChildApi):
    def get_game_definition(self):
        return self.data.rules.game_definition

    def get_hand_size(self):
        return self.data.rules.settings.hand_size
