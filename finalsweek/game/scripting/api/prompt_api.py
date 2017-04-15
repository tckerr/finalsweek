from game.scripting.api.sandbox_api import SandboxApi

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

    def prompt_actor_choice(self, actor_set, answer_key):
        return self.__answer_or_prompt(actor_set, answer_key, "id", "id")

    def prompt_seat_choice(self, seat_set, answer_key):
        return self.__answer_or_prompt(seat_set, answer_key, "coordinates_str", "id")

    def prompt_number_choice(self, number_set, answer_key):
        return self.__answer_or_prompt(number_set, answer_key)

    # ~--[private]--~

    def __answer_or_prompt(self, item_set, answer_key, display_field=None, unique_field=None):
        if self.__prompt_is_answered(answer_key):
            answer = self.answers[answer_key]
            for item in item_set:
                if unique_field:
                    value = getattr(item, unique_field)
                    if answer.__class__(getattr(item, unique_field)) == answer:
                        return item
                else:
                    if answer.__class__(item) == answer:
                        return item

            print("No item in", item_set, "Matches", unique_field, "of", answer)
            raise Exception("Invalid answer")
        else:
            prompt = self.__build_prompt(answer_key, item_set, unique_field, display_field)
            raise PromptException(prompt)

    def __prompt_is_answered(self, answer_key):
        return answer_key in self.answers

    def __build_prompt(self, answer_key, item_set, unique_field=None, display_field=None):
        new_prompt = {
            answer_key: [
                {
                    "display": getattr(item, display_field) if display_field else item,
                    "id": getattr(item, unique_field) if unique_field else item,
                    "item": item
                } for item in item_set
            ]
        }        
        return Prompt(answered=self.answers, pending=new_prompt)
