from datetime import datetime

from game.configuration.definitions import GameflowMessageType, LogLevel, LogType
from game.program_api.message_api import GameflowMessage
from game.scripting.api.program_child_api import ProgramChildApi
from logger import Logger


class StageApi(ProgramChildApi):
    def list_stages(self):
        return self.data.gameflow.stages

    def create_stage(self, stage_type):
        return self.data.gameflow.add_stage(stage_type)

    def complete_stage(self, stage_id):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                return self._complete(stage)

    def _complete(self, stage):
        stage.completed = datetime.utcnow()
        self.program_api.messenger.dispatch(GameflowMessage(GameflowMessageType.Stage))
        self.log_stage_complete(stage)

    @staticmethod
    def log_stage_complete(stage):
        message = "Stage Complete: {stage_type}".format(stage_type=stage.stage_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)
