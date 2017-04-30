from game.scripting.api.program_child_api import ProgramChildApi
from game.systems.phase_handlers.phase_handler_resolver import PhaseHandlerResolver


class PhaseApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.phase_handler_resolver = PhaseHandlerResolver(self.program_api)

    def create_phase(self, stage_id, phase_type):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                new_phase = stage.add_phase(phase_type)
                self.phase_handler_resolver.on_create(new_phase)
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
                    self.phase_handler_resolver.on_complete(phase)
