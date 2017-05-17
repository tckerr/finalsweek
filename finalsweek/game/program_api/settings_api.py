from game.scripting.api.program_child_api import ProgramChildApi


class SettingsApi(ProgramChildApi):
    def get_game_definition(self):
        return self.data.rules.game_definition

    def get_hand_size(self):
        return self.data.rules.settings.hand_size

    def get_grades_per_row(self):
        return self.data.rules.settings.grades_per_row

    def get_trouble_per_row(self):
        return self.data.rules.settings.trouble_per_row
