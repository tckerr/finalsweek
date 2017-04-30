from game.systems.phase_grade_scorer import PhaseGradeScorer
from game.systems.phase_handlers.phase_handler_base import PhaseHandlerBase
from game.systems.phase_trouble_scorer import PhaseTroubleScorer


class ClasstimePhaseHandler(PhaseHandlerBase):
    def __init__(self, api):
        super().__init__(api)
        self.phase_trouble_scorer = PhaseGradeScorer(api)
        self.phase_grade_scorer = PhaseTroubleScorer(api)

    def on_create(self, phase):
        super().on_create(phase)

    def on_complete(self, phase):
        self.phase_grade_scorer.score()
        self.phase_trouble_scorer.score()
        super().on_complete(phase)