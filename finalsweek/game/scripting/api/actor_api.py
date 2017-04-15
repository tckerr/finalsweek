from game.scripting.api.sandbox_api import SandboxApi

class ActorApi(SandboxApi):

    def __init__(self, *args, **kwargs):
        super(ActorApi, self).__init__(*args, **kwargs)

    def get_actors(self):
        return self.repo.actors()

    def get_requestor(self):
        return self.repo.requestor()

    def get_all_but_requestor(self):
        return list(filter(lambda a: a.id != self.repo.requestor_id, self.repo.actors()))

    def get_adjacent_actors(self, target_actor):
        actors = self.repo.actors()
        results = []
        for a in actors:
            proximate_column = abs(a.student.seat.column - target_actor.student.seat.column) <= 1
            proximate_row = abs(a.student.seat.row - target_actor.student.seat.row) <= 1
            if proximate_column and proximate_row:
                results.append(a)
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