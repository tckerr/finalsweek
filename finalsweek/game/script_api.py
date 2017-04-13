from django.db import transaction, models
from game.models import Student, Seat

class SaveQueue(list):

    def append(self, item):
        if item not in self:
            return super(SaveQueue, self).append(item)

class Repository(object):
    
    def students(self, **kwargs):
        return self.__model_list(Student, kwargs)

    def seats(self, **kwargs):
        return self.__model_list(Seat, kwargs)

    def __model_list(self, model_class, kwargs):
        return list(model_class.objects.filter(**kwargs))

class SandboxApi(object):
    def __init__(self, save_queue, repository):
        self.save_queue = save_queue
        self.repo = repository

class StudentApi(SandboxApi):

    def get_students(self, filters={}):
        return self.repo.students(**filters)

    def get_adjacent_students(self, target_student, filters=None):
        students = self.repo.students(**filters)
        results = []
        for s in students:
            proximate_column = abs(s.seat.column - target_student.seat.column) <= 1
            proximate_row = abs(s.seat.row - target_student.seat.row) <= 1
            if proximate_column and proximate_row:
                results.append(s)
        return results

    def set_grades(self, student, value):
        student.grades = value
        student.grades = min(0, student.grades)
        self.save_queue.append(student)

    def add_grades(self, student, value):
        student.grades += value
        student.grades = min(0, student.grades)
        self.save_queue.append(student)

    def set_popularity(self, student, value):
        student.popularity = value
        student.popularity = min(0, student.popularity)
        self.save_queue.append(student)

    def add_popularity(self, student, value):
        student.popularity += value
        student.popularity = min(0, student.popularity)
        self.save_queue.append(student)

    def set_trouble(self, student, value):
        student.trouble = value
        student.trouble = min(0, student.trouble)
        self.save_queue.append(student)

    def add_trouble(self, student, value):
        student.trouble += value
        student.trouble = min(0, student.trouble)
        self.save_queue.append(student)

    def set_torment(self, student, value):
        student.torment = value
        student.torment = min(0, student.torment)
        self.save_queue.append(student)

    def add_torment(self, student, value):
        student.torment += value
        student.torment = min(0, student.torment)
        self.save_queue.append(student)

    def draw_actioncard(self, student): pass    
    def give_action_card(self, student, action_card): pass
    def give_afterschool_card(self, student, afterschool_card): pass
    def give_discipline_card(self, student, discipline_card): pass


class SeatApi(SandboxApi):

    def get_seats(self, filters=None): pass
    def get_filled_seats(self, filters=None): pass
    def get_empty_seats(self, filters=None): pass
    def get_adjacent_seats(self, seat, filters=None): pass

class PromptException(Exception): 
    def __init__(self, prompt, *a, **k):
        self.prompt = prompt
        return super(PromptException, self).__init__(*a, **k)


class PromptApi(SandboxApi):

    def __init__(self, answers, *a, **k):
        self.answers = answers
        return super(PromptApi, self).__init__(*a, **k)    

    def prompt_student_choice(self, actor, student_set, answer_key):
        return self.__answer_or_prompt(actor, student_set, answer_key, "id", "name")

    def prompt_seat_choice(self, actor, seat_set, answer_key):
        return self.__answer_or_prompt(actor, seat_set, answer_key, "id", "coordinates_str")


    # ~--[private]--~

    def __answer_or_prompt(self, actor, item_set, answer_key, unique_field, display_field):
        if answer_key in self.answers:
            answer = self.answers[answer_key]
            for item in item_set:
                if getattr(item, unique_field) == answer:
                    return item
            raise Exception("Invalid answer")
        else:
            prompt = self.__build_prompt(answer_key, item_set, unique_field, display_field)
            raise PromptException(prompt)

    def __build_prompt(self, answer_key, item_set, unique_field, display_field):
        return {
            "answer_key": answer_key,
            "options": [
                {
                    "display": getattr(item, display_field),
                    "id": getattr(item, unique_field),
                    "item": item
                } for item in item_set
            ]
        }



class TrustedScriptRunner(object):

    def __init__(self):
        pass

    def run(self, script, answers):

        save_queue = SaveQueue()
        repository = Repository()
        student_api = StudentApi(save_queue, repository)
        seat_api = SeatApi(save_queue, repository)
        prompt_api = PromptApi(answers, save_queue, repository)

        try:
            exec(script, {
                '__answers__': answers,
                'StudentApi': student_api,
                'SeatApi': seat_api,
                'PromptApi': prompt_api,
            }, {})
        except PromptException as e:
            pass # TODO: handle prompts

        with transaction.atomic():
            for item in save_queue:
                if issubclass(item, models.Model):
                    item.save()

