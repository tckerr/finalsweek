from game.definitions import OperationType
from game.operation.decorators import accepts_operation
from game.scripting.api.program_child_api import ProgramChildApi
from trace.definitions import LogLevel, LogType
from trace.logger import Logger


class StudentApi(ProgramChildApi):
    def list_students(self):
        for seat in self.data.seats:
            student = seat.student
            if student is not None:
                yield student

    def get_student(self, student_id):
        for student in self.list_students():
            if student.id == student_id:
                return student
        raise Exception("Student not found: {}".format(student_id))

    @accepts_operation(OperationType.ModifySeat)
    def move_student_to_empty_seat(self, operation):
        operation = self._mutate(operation)
        seat = self.program_api.seats.get_seat(operation.destination_seat_id)
        student = self.get_student(operation.targeted_student_id)
        old_seat = student.seat
        assert seat.empty
        seat.student = student
        old_seat.student = None
        self._log_operation(student, seat, old_seat)

    @accepts_operation(OperationType.ModifySeat)
    def swap_seat(self, operation):
        operation = self._mutate(operation)
        student_a_id = operation.targeted_student_id
        seat_b_id = operation.destination_seat_id
        student_a = self.get_student(student_a_id)
        seat_a = student_a.seat
        seat_b = self.program_api.seats.get_seat(seat_b_id)
        student_b = seat_b.student

        seat_b.student = student_a
        seat_a.student = student_b

        self._log_operation(student_a, seat_a, seat_b)
        self._log_operation(student_b, seat_b, seat_a)

    @staticmethod
    def _log_operation(student, seat, old_seat):
        template = "Modified student {student} seat. Was: {old_coords}, now is: {coords}"
        Logger.log(template.format(
            student=student.actor_info,
            old_coords=old_seat.coordinates_str_readable,
            coords=seat.coordinates_str_readable
        ), level=LogLevel.Debug, log_type=LogType.Operational)
