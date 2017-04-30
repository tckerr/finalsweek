from game.systems.draw_manager import DrawManager
from game.systems.phase_handlers.phase_handler_base import PhaseHandlerBase


class AccumulationPhaseHandler(PhaseHandlerBase):
    def __init__(self, api) -> None:
        super().__init__(api)
        self.draw_manager = DrawManager()

    def on_create(self, phase):
        super().on_create(phase)
        actors = self.api.actors.list()
        for actor in actors:
            self.draw_manager.refill_hand(actor, self.api)