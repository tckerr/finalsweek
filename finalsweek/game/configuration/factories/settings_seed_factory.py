from game.configuration.settings import base_settings


class SettingsSeedFactory(object):
    @staticmethod
    def create():
        # todo: pass this in
        return base_settings
