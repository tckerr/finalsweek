from game.systems.phase_handlers.phase_handler_base import PhaseHandlerBase


class DismissalPhaseHandler(PhaseHandlerBase):
    def __init__(self, api):
        super().__init__(api)

    def on_create(self, phase):
        super().on_create(phase)

    def on_complete(self, phase):
        super().on_complete(phase)