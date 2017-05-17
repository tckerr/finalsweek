from game.configuration.definitions import GameflowTypeMutationGameflowBindingMap
from game.document.document_factories.phase_factory import PhaseFactory
from game.operation.mutation_adapter import MutationAdapter
from game.scripting.api.program_child_api import ProgramChildApi
from game.systems.phase_handlers.phase_handler_resolver import PhaseHandlerResolver


class PhaseApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.mutation_adapter = MutationAdapter()
        self.phase_handler_resolver = PhaseHandlerResolver(self.program_api)
        self.phase_factory = PhaseFactory()

    def create_phase(self, stage_id, phase_type):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                return self.create_phase_for_stage(phase_type, stage)

    def create_phase_for_stage(self, phase_type, stage):
        binding = GameflowTypeMutationGameflowBindingMap.get(phase_type)
        mutation_queue = self._pop_mutation_queue(binding)
        new_phase = self.phase_factory.create(phase_type, stage, mutation_queue)
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

    def _pop_mutation_queue(self, binding):
        if binding not in self.data.mutation_queue:
            return []
        result = self.data.mutation_queue[binding].mutations
        self.data.mutation_queue[binding].mutations = []
        return result
