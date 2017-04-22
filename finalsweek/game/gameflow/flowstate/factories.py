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
        result = flowstate.turn or self.__create_turn(api, phase, flowstate.actor)
        return result

    @staticmethod
    def __create_stage(api, stage_type):
        return api.stages.create_stage(stage_type)

    @staticmethod
    def __create_phase(api, stage, phase_type):
        return api.phases.create_phase(stage.id, phase_type)

    @staticmethod
    def __create_turn(api, phase, actor):
        return api.turns.create_turn(phase.id, actor.id)
