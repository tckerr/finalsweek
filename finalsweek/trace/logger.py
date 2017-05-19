import atexit
import sys
import uuid

import settings as django_settings
from configuration import settings
from configuration.settings import bcolors
from trace.definitions import LogLevel, LogType


def log(*a, **k):
    return Logger.log(*a, **k)


def write_to_disk(file_name):
    with open(file_name, "a+") as file:
        file.write(global_vars["log_txt"])


def register_exit_hook(session_id):
    if settings.logging["as_file"]:
        logger_file_name = django_settings.FINALSWEEK_LOG_DIR + (session_id or str(uuid.uuid4())) + ".txt"
        atexit.register(write_to_disk, logger_file_name)


global_vars = {
    "log_txt": ""
}


class LogOptions(object):
    def __init__(self, options) -> None:
        super().__init__()
        self.as_file = options["as_file"]
        self.print_output = options["print_output"]
        self.log_level = options["log_level"]
        self.disabled = options["disabled"]
        self.log_type_prefixes = options["log_type_prefixes"]
        self.log_type_colors = options["log_type_colors"]


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
            prefix = self.get_log_type_prefix(log_type)
            color = self.get_log_type_color(log_type)
            if self.options.as_file:
                self.queue_for_write("\n" + prefix + " ".join([str(arg) for arg in args]))
            if self.options.print_output:
                sys.stdout.write(color + prefix)
                print(*(args + (bcolors.ENDC,)))

    def should_log(self, level, log_type):
        return self.options.log_level <= level \
               and log_type not in self.options.disabled

    def queue_for_write(self, string):
        self.global_vars["log_txt"] += string

    def get_log_type_prefix(self, log_type):
        return self.options.log_type_prefixes.get(log_type, "") + " "

    def get_log_type_color(self, log_type):
        return self.options.log_type_colors.get(log_type, "")


