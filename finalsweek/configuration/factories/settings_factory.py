from configuration.settings import base_settings


class SettingsFactory(object):
    @staticmethod
    def create():
        # todo: pass this in
        return base_settings
