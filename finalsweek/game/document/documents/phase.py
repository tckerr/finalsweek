from datetime import datetime

from game.configuration.definitions import PhaseTypeName, GameflowMessageType, LogLevel, LogType
from game.document.documents.document_base import DocumentBase
from game.document.documents.prompt import Prompt
from game.document.documents.turn import Turn
from game.program_api.message_api import GameflowMessage
from game.systems.draw_manager import DrawManager
from game.systems.phase_grade_scorer import PhaseGradeScorer
from game.systems.phase_trouble_scorer import PhaseTroubleScorer
from logger import Logger
from util.random import random_id


class PhaseHandlerBase(object):
    def __init__(self, api) -> None:
        super().__init__()
        self.api = api

    def on_create(self, phase):
        self._log_phase_created(phase)

    def on_complete(self, phase):
        phase.completed = datetime.utcnow()
        self.api.messenger.dispatch(GameflowMessage(GameflowMessageType.Phase))
        self._log_phase_complete(phase)

    @staticmethod
    def _log_phase_created(phase):
        message = "Phase Created: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)

    @staticmethod
    def _log_phase_complete(phase):
        message = "Phase Complete: {phase_type}".format(phase_type=phase.phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.Gameflow)


class AccumulationPhaseHandler(PhaseHandlerBase):
    def __init__(self, api) -> None:
        super().__init__(api)
        self.draw_manager = DrawManager()

    def on_create(self, phase):
        super().on_create(phase)
        actors = self.api.actors.list()
        for actor in actors:
            self.draw_manager.refill_hand(actor, self.api)


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


class PhaseHandlerResolver(object):
    _map = {
        PhaseTypeName.Classtime:    ClasstimePhaseHandler,
        PhaseTypeName.Accumulation: AccumulationPhaseHandler
    }

    def resolve(self, phase_type, api):
        cls = self._map.get(phase_type, PhaseHandlerBase)
        return cls(api)


class Phase(DocumentBase):
    _field_definitions = {
        "id":         str,
        "phase_type": str,
        "completed":  datetime,
        "turns":      Turn
    }

    @property
    def stage(self):
        return self._parent

    def __init__(self, base_data, parent=None):
        self.phase_type = None
        super().__init__(base_data, parent)
        self.phase_handler_resolver = PhaseHandlerResolver()

    def create_turn(self, actor_id):
        turn_data = {
            "id":        random_id(),
            "actor_id":  actor_id,
            "log":       [],
            "completed": None,
            "prompt":    self.create_prompt()
        }
        cls = self._field_definitions["turns"]
        turn = cls(turn_data, parent=self)
        self.turns.append(turn)
        return turn

    @staticmethod
    def create_prompt():
        return Prompt({
            "id":     random_id(),
            "open":   {},
            "closed": {}
        })

    def on_create(self, api):
        handler = self.phase_handler_resolver.resolve(self.phase_type, api)
        handler.on_create(self)

    def on_complete(self, api):
        handler = self.phase_handler_resolver.resolve(self.phase_type, api)
        handler.on_complete(self)
