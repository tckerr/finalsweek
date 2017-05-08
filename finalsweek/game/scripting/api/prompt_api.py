from game.scripting.api.sandbox_api import SandboxApi
from trace.logger import log


class PromptException(Exception):
    def __init__(self, prompt):
        self.prompt = prompt


class PromptApi(SandboxApi):
    def __init__(self, prompt, *a, **k):
        self.prompt = prompt
        super().__init__(*a, **k)

    def prompt_student_choice(self, student_set, answer_key):
        return self.__answer_or_prompt(student_set, answer_key, display_field="id", unique_field="id")

    def prompt_actor_choice(self, actor_set, answer_key):
        return self.__answer_or_prompt(actor_set, answer_key, display_field="name", unique_field="id")

    def prompt_seat_choice(self, seat_set, answer_key):
        return self.__answer_or_prompt(seat_set, answer_key, display_field="coordinates_str", unique_field="id")

    def prompt_number_choice(self, number_set, answer_key):
        return self.__answer_or_prompt(number_set, answer_key)

    # ~--[private]--~

    def __answer_or_prompt(self, item_set, answer_key, display_field=None, unique_field=None):
        if self.__prompt_is_answered(answer_key):
            answer = self.prompt.closed[answer_key]
            for item in item_set:
                if unique_field:
                    value = getattr(item, unique_field)
                    if answer.__class__(value) == answer:
                        return item
                else:
                    if answer.__class__(item) == answer:
                        return item
            log("No item in", item_set, "Matches", unique_field, "of", answer)
            raise Exception("Invalid answer")
        else:
            prompt = self.__build_prompt(answer_key, item_set, unique_field, display_field)
            raise PromptException(prompt)

    def __prompt_is_answered(self, answer_key):
        return answer_key in self.prompt.closed

    def __build_prompt(self, answer_key, item_set, unique_field=None, display_field=None):
        from game.document.documents.document_base import DocumentBase
        options = []
        for item in item_set:
            display = getattr(item, display_field) if display_field else item
            unique_field_value = getattr(item, unique_field) if unique_field else item
            options.append({
                "display": display,
                "id":      unique_field_value,
                "item":    item if not issubclass(item.__class__, DocumentBase) else item.data
            })

        return {
            "closed": self.prompt.closed,
            "open":   {
                answer_key: options
            }
        }
