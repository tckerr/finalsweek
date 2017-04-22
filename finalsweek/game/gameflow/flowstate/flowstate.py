class Flowstate(object):
    def __init__(self, stage_type, actual_stage, phase_type, actual_phase, actor, actual_turn):
        self.stage_type = stage_type
        self.stage = actual_stage
        self.phase_type = phase_type
        self.phase = actual_phase
        self.actor = actor
        self.turn = actual_turn
        self.pending = not self.game_over

    @property
    def game_over(self):
        return self.stage_type is None

class CompletedFlowstate(object):
    def __init__(self):
        self.pending = False