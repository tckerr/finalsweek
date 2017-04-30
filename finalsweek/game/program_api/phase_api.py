from datetime import datetime

from game.configuration.definitions import GameflowMessageType, LogLevel, LogType, PhaseTypeName
from game.program_api.message_api import GameflowMessage
from game.scripting.api.program_child_api import ProgramChildApi
from game.systems.phase_grade_scorer import PhaseGradeScorer
from game.systems.phase_trouble_scorer import PhaseTroubleScorer
from logger import Logger


class PhaseApi(ProgramChildApi):

    def create_phase(self, stage_id, phase_type):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                new_phase = stage.add_phase(phase_type)
                new_phase.on_create(self.program_api)
                return new_phase

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
                    return phase.on_complete(self.program_api)

