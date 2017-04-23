from game.operation.operator_eligible import receives_operation
from game.scripting.api.base import ProgramChildApi


class StudentApi(ProgramChildApi):
    @receives_operation
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

    def move_student_to_empty_seat(self, student_id, seat_id):
        seat = self.program_api.seats.get_seat(seat_id)
        student = self.get_student(student_id)
        old_seat = student.seat
        assert seat.empty
        seat.student = student
        old_seat.student = None

    def swap_seat(self, student_a_id, seat_b_id):
        student_a = self.get_student(student_a_id)
        seat_a = student_a.seat
        seat_b = self.program_api.seats.get_seat(seat_b_id)
        student_b = seat_b.student

        seat_b.student = student_a
        seat_a.student = student_b
