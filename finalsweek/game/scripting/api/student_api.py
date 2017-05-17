from game.configuration.definitions import Tag
from game.operation.operations.modify_seat import ModifySeat
from game.scripting.api.sandbox_api import SandboxApi


class StudentApi(SandboxApi):
    def get_students(self):
        return self._sort_by_id(self.repo.students())

    def get_controlled_students(self):
        results = filter(lambda s: s.controlled, self.repo.students())
        return self._sort_by_id(results)

    def get_all_but_requestor(self):
        results = filter(lambda s: not s.controlled or s.actor.id != self.repo.requestor_id, self.repo.students())
        return self._sort_by_id(results)

    def get_adjacent_students(self, target_student):
        students = self.repo.students()
        results = []
        for s in students:
            proximate_column = abs(s.seat.column - target_student.seat.column) <= 1
            proximate_row = abs(s.seat.row - target_student.seat.row) <= 1
            if proximate_column and proximate_row and (proximate_column + proximate_row) > 0:
                results.append(s)
        return self._sort_by_id(results)

    def get_immediate_students(self, target_student):
        students = self.repo.students()
        results = []
        for s in students:
            diff_col = abs(s.seat.column - target_student.seat.column)
            diff_row = abs(s.seat.row - target_student.seat.row)
            if diff_col + diff_row == 1:
                results.append(s)
        return self._sort_by_id(results)

    def move_to_empty_seat(self, student, seat):
        default_tags = self.repo.default_tags
        operation = ModifySeat(
            destination_seat_id=seat.id,
            targeted_student_id=student.id,
            tags=default_tags.union({Tag.Seat})
        )
        self.program_api.students.move_student_to_empty_seat(operation=operation)

    def swap_seat(self, student, seat):
        default_tags = self.repo.default_tags
        operation = ModifySeat(
            destination_seat_id=seat.id,
            targeted_student_id=student.id,
            tags=default_tags.union({Tag.Seat})
        )
        self.program_api.students.swap_seat(operation=operation)

    def _sort_by_id(self, students):
        return list(sorted(students, key=lambda student: student.id))