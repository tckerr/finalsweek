from game.actions import DrawAction

class AutomaticActionResolver(object):

    def resolve(self, turn):
        if turn.phase.phase_type_id == "Accumulation":
            return DrawAction(2, turn.actor, "Action")