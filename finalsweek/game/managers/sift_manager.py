from siftpy import SiftBuilder, ContextProvider
from game.operations import max_seat_difference
import json
from game.operators import dif_abs_lte_1

class CardTargetContextProvider(ContextProvider):
    custom_operators = {
        "dif_abs_lte_1": dif_abs_lte_1
    }

    custom_operations = {
        "max_seat_difference": max_seat_difference
    }

    def __init__(self, requestor, *args, **kwargs):
        super(CardTargetContextProvider, self).__init__(*args, **kwargs)
        seats = requestor.game.seats.all()
        actors = requestor.game.actors.all()
        self.__init_context(requestor, seats, actors)

    def __init_context(self, requestor, seats, actors):
        self.context.requestor = requestor
        self.context.seats = seats
        self.context.actors = actors

    def resolve_operator(self, operator_str):
        return self.custom_operators.get(operator_str)
    
    def resolve_operation(self, operation_str):
        return self.custom_operations.get(operation_str)


class SiftManager(object):
    def __init__(self):
        self.builder = SiftBuilder()

    def parse_sift(self, sift_json_str, decisions, actor):
        context_provider = CardTargetContextProvider(actor)
        return self.get_result_or_choice(sift_json_str, decisions, context_provider)   

    def get_result_or_choice(self, sift_json_str, choices, context_provider):
        sift_dict = json.loads(sift_json_str)
        sift = self.builder.build(sift_dict, context_provider)
        #sift.print()
        for i, selected_choice in enumerate(choices):
            sift_choice = sift.get_choice()
            if sift_choice is None:
                raise Exception("A choice was given even though none are available.")
            # print(sift_choice.question)
            if i <= len(choices) - 1:
                sift_choice.choose(selected_choice)
            else:
                # we have an unchose choice, so return it
                return choice
        potential_choice = sift.get_choice()
        if potential_choice:
            return potential_choice
        return sift.results()