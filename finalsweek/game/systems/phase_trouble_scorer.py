from game.configuration.definitions import OperatorType, Tag, LogLevel, LogType
from game.operation.operations.modify_attribute import ModifyAttribute
from logger import Logger


class PhaseTroubleScorer(object):
    def __init__(self, program_api) -> None:
        super().__init__()
        self.program_api = program_api

    def score(self):
        actors = self.program_api.actors.list()
        trouble_per_row = self.program_api.settings.get_trouble_per_row()
        operation_tags = self._operation_tags()
        for actor in actors:
            self._remove_trouble_from_actor(actor, trouble_per_row, operation_tags)

    def _remove_trouble_from_actor(self, actor, trouble_per_row, operation_tags):
        value = self._calculate_phase_trouble_score(trouble_per_row, actor)
        operation = ModifyAttribute(
            operator=OperatorType.Add,
            value=value,
            targeted_actor_id=actor.id,
            tags=operation_tags
        )
        operation = self.program_api.actors.add_trouble(operation=operation)
        self._log_process(actor, operation.value)

    @staticmethod
    def _calculate_phase_trouble_score(trouble_per_row, actor):
        return trouble_per_row * (1 + actor.seat.row)

    @staticmethod
    def _operation_tags():
        return {Tag.Trouble, Tag.TroublePerTurn}

    @staticmethod
    def _log_process(actor, value):
        template = "Actor {} gained {} trouble at the end of the phase for being in seat {}."
        message = template.format(actor.label, value, actor.seat.coordinates_str_readable)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
