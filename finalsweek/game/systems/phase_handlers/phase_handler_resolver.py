from game.configuration.definitions import PhaseTypeName
from game.systems.phase_handlers.accumulation_phase_handler import AccumulationPhaseHandler
from game.systems.phase_handlers.classtime_phase_handler import ClasstimePhaseHandler
from game.systems.phase_handlers.dismissal_phase_handler import DismissalPhaseHandler
from game.systems.phase_handlers.phase_handler_base import PhaseHandlerBase


class PhaseHandlerResolver(object):
    _map = {
        PhaseTypeName.Classtime:    ClasstimePhaseHandler,
        PhaseTypeName.Accumulation: AccumulationPhaseHandler,
        PhaseTypeName.Dismissal:    DismissalPhaseHandler
    }

    def __init__(self, api) -> None:
        super().__init__()
        self.api = api

    def _resolve(self, phase_type, api):
        cls = self._map.get(phase_type, PhaseHandlerBase)
        return cls(api)

    def on_create(self, phase):
        resolver = self._resolve(phase.phase_type, self.api)
        return resolver.on_create(phase)

    def on_complete(self, phase):
        resolver = self._resolve(phase.phase_type, self.api)
        return resolver.on_complete(phase)
