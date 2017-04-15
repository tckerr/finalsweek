from game.scripting.api.sandbox_api import SandboxApi
from game.factories import SeatFactory

class StudentApi(SandboxApi):

    def __init__(self, *args, **kwargs):
        self.seat_factory = SeatFactory()
        super(StudentApi, self).__init__(*args, **kwargs)

    def get_students(self):
        return self.repo.students()

    def get_requestor(self):
        return self.repo.requestor()

    def get_all_but_requestor(self):
        return list(filter(lambda s: s.id != self.repo.requestor_id, self.repo.students()))

    def get_adjacent_students(self, target_student):
        students = self.repo.students()
        results = []
        for s in students:
            proximate_column = abs(s.seat.column - target_student.seat.column) <= 1
            proximate_row = abs(s.seat.row - target_student.seat.row) <= 1
            if proximate_column and proximate_row:
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

    def set_grades(self, student, value):
        student.grades = value
        student.grades = max(0, student.grades)
        self.save_queue.append(student)

    def add_grades(self, student, value):
        student.grades += value
        student.grades = max(0, student.grades)
        self.save_queue.append(student)

    def set_popularity(self, student, value):
        student.popularity = value
        student.popularity = max(0, student.popularity)
        self.save_queue.append(student)

    def add_popularity(self, student, value):
        student.popularity += value
        student.popularity = max(0, student.popularity)
        self.save_queue.append(student)

    def set_trouble(self, student, value):
        student.trouble = value
        student.trouble = max(0, student.trouble)
        self.save_queue.append(student)

    def add_trouble(self, student, value):
        student.trouble += value
        student.trouble = max(0, student.trouble)
        self.save_queue.append(student)

    def set_torment(self, student, value):
        student.torment = value
        student.torment = max(0, student.torment)
        self.save_queue.max(student)

    def add_torment(self, student, value):
        student.torment += value
        student.torment = max(0, student.torment)
        self.save_queue.append(student)

    def draw_actioncard(self, student): pass    
    def give_action_card(self, student, action_card): pass
    def give_afterschool_card(self, student, afterschool_card): pass
    def give_discipline_card(self, student, discipline_card): pass

    def move_to_empty_seat(self, student, seat):
        assert seat.empty
        student.seat = seat
        self.save_queue.append(student)

    def swap_seat(self, student, seat):
        assert not seat.empty
        temp_seat = self.seat_factory.create_with_id(student.game_id, 9999, 9999)

        orphan_student = seat.actor
        orphan_student.seat = temp_seat
        orphan_student.save()

        orphan_seat = student.seat
        student.seat = seat
        orphan_student.seat = orphan_seat

        temp_seat.delete()

        self.save_queue.append(student)
        self.save_queue.append(orphan_student)

