from datetime import datetime

from game.configuration.definitions import GameflowMessageType, LogLevel, LogType
from game.program_api.message_api import GameflowMessage
from game.scripting.api.program_child_api import ProgramChildApi
from game.systems.phase_grade_scorer import PhaseGradeScorer
from game.systems.phase_trouble_scorer import PhaseTroubleScorer
from logger import Logger


class PhaseApi(ProgramChildApi):
    def __init__(self, program_api):
        super().__init__(program_api)
        self.phase_grade_scorer = PhaseGradeScorer(program_api)
        self.phase_trouble_scorer = PhaseTroubleScorer(program_api)

    def create_phase(self, stage_id, phase_type):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                return stage.add_phase(phase_type)

    def get_phase_definition(self, phase_type):
        stage_definitions = self.data.rules.game_definition
        for stage_definition in stage_definitions:
            for phase_definition in stage_definition.phases:
                if phase_definition.phase_type == phase_type:
                    return phase_definition

    def complete_phase(self, phase_id):
        for stage in self.data.gameflow.stages:
            for phase in stage.phases:
                if phase.id == phase_id:
                    return self._complete(phase)

    def _complete(self, phase):
        phase.completed = datetime.utcnow()
        self.phase_grade_scorer.score()
        self.phase_trouble_scorer.score()
        self.program_api.messenger.dispatch(GameflowMessage(GameflowMessageType.Phase))
        self.log_phase_complete(phase)

    @staticmethod
    def log_phase_complete(phase):
        message = "Phase Complete: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)

