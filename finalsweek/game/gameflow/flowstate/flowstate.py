class Flowstate(object):
    def __init__(self, stage_type, actual_stage, phase_type, actual_phase, actor, actual_turn):
        self.stage_type = stage_type
        self.stage = actual_stage
        self.phase_type = phase_type
        self.phase = actual_phase
        self.actor = actor
        self.turn = actual_turn
        self.pending = not self.game_over
        self.autocomplete_phase = False

    @property
    def game_over(self):
        return self.stage_type is None


class AutocompletingPhaseFlowstate(Flowstate):
    def __init__(self, stage_type, actual_stage, phase_type):
        super().__init__(stage_type, actual_stage, phase_type, None, None, None)
        self.autocomplete_phase = True


class CompletedFlowstate(object):
    def __init__(self):
        self.pending = False
