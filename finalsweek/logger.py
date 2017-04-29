import uuid

import settings as django_settings
from game.configuration import settings
from game.configuration.definitions import LogType, LogLevel
from util.util import guid

session_guid = str(uuid.uuid4()) # guid()


def log(*a, **k):
    return Logger.log(*a, **k)


class LogOptions(object):
    def __init__(self, options) -> None:
        super().__init__()
        self.as_file = options["as_file"]
        self.print_output = options["print_output"]
        self.log_level = options["log_level"]
        self.disabled = options["disabled"]
        self.session_guid = session_guid


class Logger(object):
    @classmethod
    def log(cls, *a, **k):
        logger = cls(settings.logging)
        logger._log(*a, **k)

    def __init__(self, options=None) -> None:
        self.options = LogOptions(options)

    def _log(self, *args, level=LogLevel.Verbose, log_type=LogType.General):
        if self.should_log(level, log_type):
            if self.options.as_file:
                self.write_to_file(args)
            if self.options.print_output:
                print(*args)

    def write_to_file(self, args):
        with open(self._file_name, "a+") as file:
            file.write("\n" + " ".join([str(arg) for arg in args]))

    def should_log(self, level, log_type):
        return self.options.log_level >= level \
               and log_type not in self.options.disabled

    @property
    def _file_name(self):
        return django_settings.FINALSWEEK_LOG_DIR + self.options.session_guid + ".txt"
