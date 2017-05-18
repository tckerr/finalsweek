from game.gameflow.flowstate.base_flowstate_resolver import BaseFlowstateResolver
from game.gameflow.flowstate.flowstate import Flowstate, CompletedFlowstate, AutocompletingPhaseFlowstate


class FlowstateTurnResolver(BaseFlowstateResolver):
    def resolve(self, actor, actual_stage, stage_type, actual_phase, phase_type, turn_count, api):
        for turn_number in range(0, turn_count):
            actual_turn = self.__get_turn_at_set(actual_phase, actor, turn_number)
            if not actual_stage or not actual_phase or not actual_turn or actual_turn.completed is None:
                return Flowstate(stage_type, actual_stage, phase_type, actual_phase, actor, actual_turn)
        return CompletedFlowstate()

    @staticmethod
    def __get_turn_at_set(phase, actor, set_number):
        if not phase:
            return None
        results = list(filter(lambda turn: turn.actor_id == actor.id, phase.turns))
        if len(results) < set_number + 1:
            return None
        return results[set_number]


class FlowstatePhaseResolver(BaseFlowstateResolver):
    def __init__(self):
        self.flowstate_turn_resolver = FlowstateTurnResolver()

    def resolve(self, actors, actual_stage, stage_type, phase_set, stage_definition, api):
        for phase_definition in stage_definition.phases:
            phase_type = phase_definition.phase_type
            actual_phase = self.__get_phase_at_set(actual_stage, phase_type, phase_set)
            if actual_phase and actual_phase.completed is not None:
                continue
            for actor in actors:
                flowstate = self.flowstate_turn_resolver.resolve(actor, actual_stage, stage_type, actual_phase,
                                                                 phase_type, phase_definition.turn_sets, api)
                if flowstate.pending:
                    return flowstate
            if not actual_phase:
                return AutocompletingPhaseFlowstate(stage_type, actual_stage, phase_type)
            self._complete_phase(actual_phase, api)
        return CompletedFlowstate()

    @staticmethod
    def __get_phase_at_set(stage, phase_type, set_number):
        if not stage:
            return None
        results = list(filter(lambda phase: phase.phase_type == phase_type, stage.phases))
        if len(results) < set_number + 1:
            return None
        return results[set_number]


class FlowstateStageResolver(BaseFlowstateResolver):
    def __init__(self):
        self.flowstate_phase_resolver = FlowstatePhaseResolver()

    def resolve(self, actors, stages, stage_definition, api):
        stage_type = stage_definition.stage_type
        actual_stage = self.__get_stage_by_type(stages, stage_type)
        if not actual_stage or actual_stage.completed is None:
            for phase_set in range(0, stage_definition.phase_sets):
                flowstate = self.flowstate_phase_resolver.resolve(actors, actual_stage, stage_type, phase_set,
                                                                  stage_definition, api)
                if flowstate.pending:
                    return flowstate
            self._complete_stage(actual_stage, api)
        return CompletedFlowstate()

    @staticmethod
    def __get_stage_by_type(stages, stage_type):
        results = list(filter(lambda stage: stage.stage_type == stage_type, stages))
        return results[0] if results else None


class FlowstateResolver(object):
    def __init__(self):
        self.flowstate_stage_resolver = FlowstateStageResolver()

    def resolve(self, actors, stages, game_definition, api):
        for stage_definition in game_definition:
            flowstate = self.flowstate_stage_resolver.resolve(actors, stages, stage_definition, api)
            if flowstate.pending:
                return flowstate
        return CompletedFlowstate()
