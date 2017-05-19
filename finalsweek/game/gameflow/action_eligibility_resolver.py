from game.definitions import PhaseTypeName
from game.exceptions import TurnValidationException
from game.gameflow.actions.action_card import ActionCardAction
from game.gameflow.actions.base import ActionBase
from game.gameflow.actions.discipline import DisciplineAction


class ActionEligibilityResolver(object):

    eligibility_map = {
        PhaseTypeName.ChooseSeats: (ActionBase,),
        PhaseTypeName.Classtime: (ActionCardAction,),
        PhaseTypeName.Dismissal: (DisciplineAction,),
        PhaseTypeName.AfterSchool: (ActionBase,),
    }

    def validate(self, action, turn):
        eligible = self.eligibility_map.get(turn.phase.phase_type, [])
        if action.__class__ not in eligible:
            raise TurnValidationException("Action type {} is not permitted in phase {}".format(
                action.__class__.__name__,
                turn.phase.phase_type
            ))