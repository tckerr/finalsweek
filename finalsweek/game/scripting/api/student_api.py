from game.scripting.api.sandbox_api import SandboxApi
from game.factories import SeatFactory

class StudentApi(SandboxApi):

    def __init__(self, *args, **kwargs):
        self.seat_factory = SeatFactory()
        super(StudentApi, self).__init__(*args, **kwargs)

    def get_students(self):
        return self.repo.students()

    def get_controlled_students(self):
        return list(filter(lambda s: s.controlled, self.repo.students()))

    def get_all_but_requestor(self):
        return list(filter(lambda s: not s.controlled or s.actor.id != self.repo.requestor_id, self.repo.students()))

    def get_adjacent_students(self, target_student):
        students = self.repo.students()
        results = []
        for s in students:
            proximate_column = abs(s.seat.column - target_student.seat.column) <= 1
            proximate_row = abs(s.seat.row - target_student.seat.row) <= 1
            if proximate_column and proximate_row and (proximate_column + proximate_row) > 0:
                results.append(s)
        return results

    def get_immediate_students(self, target_student):
        students = self.repo.students()
        results = []
        for s in students:
            diff_col = abs(s.seat.column - target_student.seat.column)
            diff_row = abs(s.seat.row - target_student.seat.row)
            if diff_col + diff_row == 1:
                results.append(s)
        return results

    def move_to_empty_seat(self, student, seat):
        assert seat.empty
        student.seat = seat
        self.save_queue.append(student)

    def swap_seat(self, student, seat):
        assert not seat.empty
        temp_seat = self.seat_factory.create_with_id(student.seat.game_id, 9999, 9999)

        orphan_student = seat.student
        orphan_student.seat = temp_seat
        orphan_student.save()

        orphan_new_seat = student.seat
        student.seat = seat
        student.save()
        orphan_student.seat = orphan_new_seat
        orphan_student.save()

        temp_seat.delete()

        self.save_queue.append(student)
        self.save_queue.append(orphan_student)

