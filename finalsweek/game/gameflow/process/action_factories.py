from game.actions import ActionBase, RedrawToFullAction
from game.configuration.definitions import PhaseTypeName


class ActionFactory(object):
    def create(self):
        return ActionBase()


class AccumulationActionFactory(ActionFactory):
    def create(self):
        # TODO: add other parts of accumulation
        return RedrawToFullAction()


class AutomatedActionFactory(object):
    factories = {
        PhaseTypeName.ChooseSeats:  ActionFactory,
        PhaseTypeName.Accumulation: AccumulationActionFactory,
        PhaseTypeName.Score:        ActionFactory
    }

    def create(self, phase_definition):
        factory_class = self.factories.get(phase_definition.phase_type)
        if not factory_class:
            raise Exception("Cannot automate turn of phase_type '{}' because no factory is defined "
                            "for the corresponding action.".format(phase_definition.phase_type))
        factory = factory_class()
        return factory.create()
