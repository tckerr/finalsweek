from datetime import datetime

from game.configuration.definitions import LogLevel, LogType
from logger import Logger


class PhaseHandlerBase(object):
    def __init__(self, api) -> None:
        super().__init__()
        self.api = api

    def on_create(self, phase):
        self._log_phase_created(phase)

    def on_complete(self, phase):
        phase.completed = datetime.utcnow()
        self._log_phase_complete(phase)

    @staticmethod
    def _log_phase_created(phase):
        message = "Phase Created: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)

    @staticmethod
    def _log_phase_complete(phase):
        message = "Phase Complete: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)
