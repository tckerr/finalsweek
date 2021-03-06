from game.definitions import PhaseTypeName
from game.gameflow.actions.base import ActionBase
from game.gameflow.actions.redraw import RedrawAction
from game.gameflow.actions.score import ScoreAction


class ActionFactory(object):
    def create(self):
        return ActionBase()


class ScoreActionFactory(object):
    @staticmethod
    def create():
        return ScoreAction({})


class AccumulationActionFactory(ActionFactory):
    def create(self):
        # TODO: add other parts of accumulation
        return RedrawAction()


class AutomatedActionFactory(object):
    factories = {
        PhaseTypeName.ChooseSeats:  ActionFactory,
        PhaseTypeName.Accumulation: AccumulationActionFactory,
        PhaseTypeName.Score:        ScoreActionFactory
    }

    def create(self, phase_definition):
        factory_class = self.factories.get(phase_definition.phase_type)
        if not factory_class:
            raise Exception("Cannot automate turn of phase_type '{}' because no factory is defined "
                            "for the corresponding action.".format(phase_definition.phase_type))
        factory = factory_class()
        return factory.create()
