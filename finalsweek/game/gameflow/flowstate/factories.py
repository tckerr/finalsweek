from game.gameflow.flowstate.resolvers import FlowstateResolver


class TurnFactory(object):
    def __init__(self):
        self.flowstate_resolver = FlowstateResolver()

    def get_or_create(self, api):
        actors = list(api.actors.list_actors_sorted_by_seat())
        stages = list(api.stages.list_stages())
        game_definition = api.settings.get_game_definition()
        flowstate = self.flowstate_resolver.resolve(actors, stages, game_definition, api)
        if not flowstate.pending:
            return
        stage = flowstate.stage or self.__create_stage(api, flowstate.stage_type)
        phase = flowstate.phase or self.__create_phase(api, stage, flowstate.phase_type)
        if flowstate.autocomplete_phase:
            return self._handle_autocomplete(api, phase)
        result = flowstate.turn or self.__create_turn(api, phase, flowstate.actor)
        return result

    def _handle_autocomplete(self, api, phase):
        self.__dirty = True
        api.phases.complete_phase(phase)
        return self.get_or_create(api)

    def __create_stage(self, api, stage_type):
        self.__dirty = True
        return api.stages.create_stage(stage_type)

    def __create_phase(self, api, stage, phase_type):
        self.__dirty = True
        return api.phases.create_phase(stage.id, phase_type)

    def __create_turn(self, api, phase, actor):
        self.__dirty = True
        return api.turns.create_turn(phase.id, actor.id)
