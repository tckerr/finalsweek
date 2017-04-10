class Flowstate(object):
    def __init__(self, stage_name, actual_stage, phase_name, actual_phase, actor, actual_turn):
        self.stage_name = stage_name
        self.stage = actual_stage
        self.phase_name = phase_name
        self.phase = actual_phase
        self.actor = actor
        self.turn = actual_turn
        self.pending = not self.game_over

    @property
    def game_over(self):
        return self.stage_name is None

class CompletedFlowstate(object):
    def __init__(self):
        self.pending = False