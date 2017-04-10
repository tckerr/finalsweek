from game.gameflow.flowstate.flowstate import Flowstate, CompletedFlowstate
from game.gameflow.flowstate.base_flowstate_resolver import BaseFlowstateResolver
from game.settings import settings


class FlowstateTurnResolver(BaseFlowstateResolver):

    def resolve(self, actors, actual_stage, stage_name, actual_phase, phase_name, turn_set, stage_definition):
        for actor in actors: 
            actual_turn = self.__get_turn_at_set(actual_phase, actor, turn_set)
            if not actual_stage or not actual_phase or not actual_turn or actual_turn.completed is None:
                return Flowstate(stage_name, actual_stage, phase_name, actual_phase, actor, actual_turn)
        return CompletedFlowstate()

    def __get_turn_at_set(self, phase, actor, set_number):
        if not phase:
            return None
        return self._filter_related_manager_itemset(phase.turns, actor.id, "actor_id", set_number)


class FlowstatePhaseResolver(BaseFlowstateResolver):

    def __init__(self):
        self.flowstate_turn_resolver = FlowstateTurnResolver()

    def resolve(self, actors, actual_stage, stage_name, phase_set, stage_definition):
        for phase_definition in stage_definition["phases"]:
            phase_name = phase_definition["name"]
            actual_phase = self.__get_phase_at_set(actual_stage, phase_name, phase_set)
            if actual_phase and actual_phase.completed is not None:
                continue
            for turn_set in range(0, phase_definition["turn_sets"]):
                flowstate = self.flowstate_turn_resolver.resolve(actors, actual_stage, stage_name, actual_phase, phase_name, turn_set, stage_definition)
                if flowstate.pending:
                    return flowstate  
            self._complete(actual_phase)                    
        return CompletedFlowstate()

    def __get_phase_at_set(self, stage, phase_name, set_number):
        if not stage:
            return None
        return self._filter_related_manager_itemset(stage.phases, phase_name, "phase_type_id", set_number)


class FlowstateStageResolver(BaseFlowstateResolver):

    def __init__(self):
        self.flowstate_phase_resolver = FlowstatePhaseResolver()

    def resolve(self, actors, stages, stage_definition):
        stage_name = stage_definition["name"]
        actual_stage = self.__get_stage_by_name(stages, stage_name)
        if not actual_stage or actual_stage.completed is None:       
            for phase_set in range(0, stage_definition["phase_sets"]):
                flowstate = self.flowstate_phase_resolver.resolve(actors, actual_stage, stage_name, phase_set, stage_definition)
                if flowstate.pending:
                    return flowstate    
            self._complete(actual_stage)
        return CompletedFlowstate()

    def __get_stage_by_name(self, stages, stage_name):
        return self._filter_related_manager_itemset(stages, stage_name, "stage_type_id")


class FlowstateResolver(object):

    def __init__(self):
        self.game_definition = settings["game_definition"]
        self.flowstate_stage_resolver = FlowstateStageResolver()

    def resolve(self, actors, stages):
        for stage_definition in self.game_definition:
            flowstate = self.flowstate_stage_resolver.resolve(actors, stages, stage_definition)
            if flowstate.pending:
                return flowstate
        return CompletedFlowstate()