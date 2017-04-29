import atexit
import uuid

import settings as django_settings
from game.configuration import settings
from game.configuration.definitions import LogType, LogLevel
# TODO: make this game ID
# TODO: make game only write at end


def log(*a, **k):
    return Logger.log(*a, **k)


def write_to_disk(file_name):
    with open(file_name, "a+") as file:
        file.write(global_vars["log_txt"])


global_vars = {
    "log_txt": ""
}

if settings.logging["as_file"]:
    session_guid = str(uuid.uuid4())
    logger_file_name = django_settings.FINALSWEEK_LOG_DIR + session_guid + ".txt"
    atexit.register(write_to_disk, logger_file_name)


class LogOptions(object):
    def __init__(self, options) -> None:
        super().__init__()
        self.as_file = options["as_file"]
        self.print_output = options["print_output"]
        self.log_level = options["log_level"]
        self.disabled = options["disabled"]


class Logger(object):
    @classmethod
    def log(cls, *a, **k):
        logger = cls(settings.logging)
        logger._log(*a, **k)

    def __init__(self, options=None) -> None:
        self.options = LogOptions(options)
        self.global_vars = global_vars

    def _log(self, *args, level=LogLevel.Verbose, log_type=LogType.General):
        if self.should_log(level, log_type):
            if self.options.as_file:
                self.queue_for_write("\n" + " ".join([str(arg) for arg in args]))
            if self.options.print_output:
                print(*args)

    def should_log(self, level, log_type):
        return self.options.log_level <= level \
               and log_type not in self.options.disabled

    def queue_for_write(self, string):
        self.global_vars["log_txt"] += string
