from game.models import Stage, Phase, Turn
from game.gameflow.flowstate.repositories import StagePrefetchRepository
from game.gameflow.flowstate.resolvers import FlowstateResolver

class TurnFactory(object):

    def __init__(self):
        self.stage_prefetch_repository = StagePrefetchRepository()
        self.flowstate_resolver = FlowstateResolver()

    def get_or_create(self, game):        
        actors = self.__get_sorted_actors(game)
        stages = self.stage_prefetch_repository.get(game)
        flowstate = self.flowstate_resolver.resolve(actors, stages)
        if not flowstate.pending:
            return
        stage = flowstate.stage or self.__create_stage(game, flowstate.stage_name)
        phase = flowstate.phase or self.__create_phase(stage, flowstate.phase_name)
        result = flowstate.turn or self.__create_turn(phase, flowstate.actor)
        return result

    def __get_sorted_actors(self, game):
        actors = game.actors.order_by('seat__row', 'seat__column')
        return list(actors.all())


    def __create_stage(self, game, stage_name):
        stage = Stage()
        stage.game = game
        stage.stage_type_id = stage_name
        stage.save()
        return stage

    def __create_phase(self, stage, phase_name):        
        phase = Phase()
        phase.stage = stage
        phase.phase_type_id = phase_name
        phase.save()
        return phase

    def __create_turn(self, phase, actor):
        turn = Turn()
        turn.phase = phase
        turn.actor = actor
        turn.save()
        return turn