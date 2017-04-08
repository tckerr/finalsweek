from game.actions import DrawAction
from game.settings import settings
from game.models import PileCard

class AutomaticActionResolver(object):

    def resolve(self, turn):
        if turn.phase.phase_type_id == "Accumulation":
            cards_needed = settings["hand_size"] - PileCard.objects.filter(pile=turn.actor.action_hand).count()
            effective_draw = cards_needed if cards_needed > 0 else 0
            return DrawAction(effective_draw, turn.actor, "Action")