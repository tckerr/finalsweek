from game.actions import DrawAction
from game.settings import settings

class AutomaticActionResolver(object):

    def resolve(self, turn):
        if turn.phase.phase_type_id == "Accumulation":
            cards_needed = settings["hand_size"] - turn.actor.action_hand.get_cards().count()
            effective_draw = cards_needed if cards_needed > 0 else 0
            return DrawAction(effective_draw, turn.actor, "Action")