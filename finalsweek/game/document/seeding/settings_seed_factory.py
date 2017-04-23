from game.configuration.settings import base_settings


class SettingsSeedFactory(object):
    @staticmethod
    def create():
        return base_settings
