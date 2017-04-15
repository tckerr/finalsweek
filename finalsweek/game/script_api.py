from django.db import transaction, models
from game.models import Actor, Seat

class SaveQueue(list):

    def append(self, item):
        if item not in self:
            return super(SaveQueue, self).append(item)

class Repository(object):

    def __init__(self, requestor):
        self.requestor_id = requestor.id
        self.game_id = requestor.game_id
    
    def students(self):
        if not hasattr(self, "_students_cache"):
            kwargs = {"game_id": self.game_id}
            self._students_cache = self.__model_list(Actor, kwargs)
        return self._students_cache

    def requestor(self):
        students = self.students()
        return next(filter(lambda s: s.id == self.requestor_id, students))

    def seats(self):
        if not hasattr(self, "_seats_cache"):
            kwargs = {"game_id": self.game_id}
            self._seats_cache = self.__model_list(Seat, kwargs)
        return self._seats_cache

    def __model_list(self, model_class, kwargs):
        return list(model_class.objects.filter(**kwargs))

class SandboxApi(object):
    def __init__(self, save_queue, repository):
        self.save_queue = save_queue
        self.repo = repository

class StudentApi(SandboxApi):

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
        temp_seat = Seat()
        temp_seat.row = 99999
        temp_seat.column = 99999
        temp_seat.game_id = student.game_id
        temp_seat.save()

        orphan_student = seat.actor
        orphan_student.seat = temp_seat
        orphan_student.save()

        orphan_seat = student.seat
        student.seat = seat
        orphan_student.seat = orphan_seat

        temp_seat.delete()

        self.save_queue.append(student)
        self.save_queue.append(orphan_student)


class SeatApi(SandboxApi):

    def get_seats(self):
        return self.repo.seats()

    def get_filled_seats(self):
        seats = self.get_seats()
        return list(filter(lambda s: not s.empty, seats))

    def get_empty_seats(self):
        seats = self.get_seats()
        return list(filter(lambda s: s.empty, seats))

    def get_adjacent_seats(self, seat): pass

class PromptException(Exception): 
    def __init__(self, prompt, *a, **k):
        self.prompt = prompt
        return super(PromptException, self).__init__(*a, **k)


class Prompt(object):
    def __init__(self, answered=None, pending=None):
        self.__answered = answered or {}
        self.__pending = pending or {}

    def answer(self, key, val):
        del self.__pending[key]
        self.__answered[key] = val

    @property
    def cumulative_answers(self):
        return self.__answered

    @property
    def pending(self):
        return [(k, v) for k, v in self.__pending.items()]

class PromptApi(SandboxApi):

    def __init__(self, answers, *a, **k):
        self.answers = answers
        return super(PromptApi, self).__init__(*a, **k)    

    def prompt_student_choice(self, student_set, answer_key):
        return self.__answer_or_prompt(student_set, answer_key, "id", "id")

    def prompt_seat_choice(self, seat_set, answer_key):
        return self.__answer_or_prompt(seat_set, answer_key, "id", "coordinates_str")


    # ~--[private]--~

    def __answer_or_prompt(self, item_set, answer_key, unique_field, display_field):
        if self.__prompt_is_answered(answer_key):
            answer = self.answers[answer_key]
            for item in item_set:
                value = getattr(item, unique_field)
                if answer.__class__(getattr(item, unique_field)) == answer:
                    return item
            print("No item in", item_set, "Matches", unique_field, "of", answer)
            raise Exception("Invalid answer")
        else:
            prompt = self.__build_prompt(answer_key, item_set, unique_field, display_field)
            raise PromptException(prompt)

    def __prompt_is_answered(self, answer_key):
        return answer_key in self.answers


    def __build_prompt(self, answer_key, item_set, unique_field, display_field):
        new_prompt = {
            answer_key: [
                {
                    "display": getattr(item, display_field),
                    "id": getattr(item, unique_field),
                    "item": item
                } for item in item_set
            ]
        }        
        return Prompt(answered=self.answers, pending=new_prompt)



class TrustedScriptRunner(object):

    def __init__(self):
        pass

    def run(self, actor, script, answers):

        print("        Prior to running script, requestor:", actor.id, actor.summary)
        print("        Executing with answers:", answers)
        save_queue = SaveQueue()
        repository = Repository(actor)
        student_api = StudentApi(save_queue, repository)
        seat_api = SeatApi(save_queue, repository)
        prompt_api = PromptApi(answers, save_queue, repository)
        scope_vars = dict(locals(), **globals())
        scope_vars.update({
            '__answers__': answers,
            'StudentApi': student_api,
            'SeatApi': seat_api,
            'PromptApi': prompt_api
        })

        try:
            exec(script, scope_vars, scope_vars)
        except PromptException as e:
            return self.__save_and_prompt(save_queue, e.prompt)

        return self.__save(save_queue)


    def __save(self, save_queue):
        with transaction.atomic():
            for item in save_queue:
                if issubclass(item.__class__, models.Model):
                    if item.__class__ is Actor:
                        print("        * Saving changes:", item, item.summary)
                    else:
                        print("        * Saving changes:", item)
                    item.save()


    def __save_and_prompt(self, save_queue, prompt):
        self.__save(save_queue)
        return prompt

