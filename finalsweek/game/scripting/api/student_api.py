from game.scripting.api.sandbox_api import SandboxApi


class StudentApi(SandboxApi):

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
        self.program_api.students.move_student_to_empty_seat(student.id, seat.id)

    def swap_seat(self, student, seat):
        self.program_api.students.swap_seat(student.id, seat.id)