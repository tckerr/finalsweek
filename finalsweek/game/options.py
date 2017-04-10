from game.managers.sift_manager import SiftManager
from django.contrib.contenttypes.models import ContentType
from siftpy._choice import Choice


class ArgumentChoiceBuilder(object):
    def __init__(self):
        self.sift_manager = SiftManager()

    def build(self, arg, operation_decisions, current_actor, supply_results):
        if not arg.is_sift:
            if supply_results:
                return { arg.key: [arg.value] }
        else:
            arg_decisions = operation_decisions.get(arg.id, [])
            result = self.sift_manager.parse_sift(arg.value, arg_decisions, current_actor) 
            if result.__class__ is Choice: 
                combined_decisions = arg_decisions + [result]
                return { arg.key: result } if supply_results else { arg.id: combined_decisions } 
            else:
                return { arg.key: result } if supply_results else { arg.id: arg_decisions }#ResultSet([operation_arg.key, result])  --> for actual value


class OperationChoiceBuilder(object):
    def __init__(self):
        self.arg_choice_builder = ArgumentChoiceBuilder()

    def build(self, operation, operation_set_decisions, current_actor, supply_results):
        results = {}
        operation_decisions = operation_set_decisions.get(operation.id, {})
        for arg in operation.arguments.all():
            result = self.arg_choice_builder.build(arg, operation_decisions, current_actor, supply_results)
            if result:
                results.update(result)
        return results


class CardTargetOperationSetChoiceBuilder(object):

    def __init__(self):
        self.sift_manager = SiftManager()
        self.operation_choice_builder = OperationChoiceBuilder()

   
    def build(self, current_turn, cto, card_decisions, supply_results=False):
        cto_decisions = card_decisions.get(cto.id, {})
        target_decisions = cto_decisions.get("target_decisions", [])
        operation_set_decisions = cto_decisions.get("operation_set_decisions", {})
        current_actor = current_turn.actor
        target_result = self.__build_target_result(current_actor, cto, target_decisions, supply_results)
        operation_set_result = self.__build_operation_set_result(current_actor, cto, operation_set_decisions, supply_results)
        return { 
            "target_choices": target_result,
            "operation_set_choices": operation_set_result
        }

    def __build_target_result(self, current_actor, cto, target_decisions, supply_results):        
        sift_json_str = cto.target.sift
        result = self.sift_manager.parse_sift(sift_json_str, target_decisions, current_actor)   
        if result.__class__ is Choice: 
            combined_decisions = target_decisions + [result]
            return result if supply_results else combined_decisions
        else:
            self.__assert_content_types(result, cto)
            return result if supply_results else target_decisions

    def __build_operation_set_result(self, current_actor, cto, operation_set_decisions, supply_results):
        operations = cto.operation_set.operations.all()
        return { o.id: self.operation_choice_builder.build(o, operation_set_decisions, current_actor, supply_results) for o in operations}

    def __assert_content_types(self, items, cto):
        for item in items:
            content_type = ContentType.objects.get_for_model(item.__class__)
            if content_type != cto.target.target_content_type:
                raise Exception("Target {target_desc} ({target_id}) yielded an object of type {result_content_type}, but target_content_type is {target_content_type}.".format(
                    target_desc=cto.target.description,
                    target_id=str(cto.target.id),
                    result_content_type=content_type,
                    target_content_type=cto.target.target_content_type))

class Perspective(object):
    def __init__(self, actor_id):
        self.actor_id = actor_id

class TurnSummary(object): pass

class ActionCardOptionBuilder(object):
    def __init__(self):
        self.card_target_operation_set_choice_builder = CardTargetOperationSetChoiceBuilder()

    def build(self, current_turn, card, decisions):
        card_decisions = decisions.get(card.id, {})
        card_target_operation_sets = card.card_target_operation_sets.order_by('execution_order')
        return { cto.id: self.card_target_operation_set_choice_builder.build(current_turn, cto, card_decisions) for cto in card_target_operation_sets }

class TurnOptionBuilder(object):
    # TODO, we can early exit if this isnt chosen yet
    def __init__(self):
        self.action_card_option_builder = ActionCardOptionBuilder()

    def build(self, current_turn, decisions):
        phase = current_turn.phase.phase_type_id
        if phase == "Classtime":
            action_cards = list(current_turn.actor.action_hand.cards.all())
            seen = []
            hand = []
            for card in action_cards:
                if card.name not in seen:
                    hand.append(card)
                    seen.append(card.name)
            return {
                "Action Cards": { card.name: self.action_card_option_builder.build(current_turn, card, decisions) for card in hand }
            } 
