from datetime import datetime

from trace.logger import Logger
from trace.definitions import LogLevel, LogType


class PhaseHandlerBase(object):
    def __init__(self, api) -> None:
        super().__init__()
        self.api = api

    def on_create(self, phase):
        self._log_phase_created(phase)

    def on_complete(self, phase):
        phase.completed = datetime.utcnow()
        for mutation in phase.mutations:
            self.api.actors.remove_card_in_play(mutation.id)
        self._log_phase_complete(phase)

    @staticmethod
    def _log_phase_created(phase):
        message = "Phase Created: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)

    @staticmethod
    def _log_phase_complete(phase):
        message = "Phase Complete: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)
