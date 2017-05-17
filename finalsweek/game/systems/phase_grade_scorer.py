from game.configuration.definitions import OperatorType, Tag
from game.operation.operations.modify_attribute import ModifyAttribute
from trace.logger import Logger
from trace.definitions import LogLevel, LogType


class PhaseGradeScorer(object):
    def __init__(self, program_api) -> None:
        super().__init__()
        self.program_api = program_api

    def score(self):
        actors = self.program_api.actors.list()
        grades_per_row = self.program_api.settings.get_grades_per_row()
        operation_tags = self._operation_tags()
        for actor in actors:
            self._add_grades_to_actor(actor, grades_per_row, operation_tags)

    def _add_grades_to_actor(self, actor, grades_per_row, operation_tags):
        value = self._calculate_phase_grade_score(grades_per_row, actor)
        operation = ModifyAttribute(
            operator=OperatorType.Add,
            value=value,
            targeted_actor_id=actor.id,
            tags=operation_tags
        )
        operation = self.program_api.actors.add_grades(operation=operation)
        self._log_process(actor, operation.value)

    @staticmethod
    def _calculate_phase_grade_score(grades_per_row, actor):
        return grades_per_row * (1 + actor.seat.row)

    @staticmethod
    def _operation_tags():
        return {Tag.Grades, Tag.GradesPerTurn}

    @staticmethod
    def _log_process(actor, value):
        template = "Actor {} scored {} grades at the end of the phase for being in seat {}."
        message = template.format(actor.label, value, actor.seat.coordinates_str_readable)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
