from game.managers.input.input_manager_base import InputManagerBase
from game.managers.draw_manager import ActionHandDrawManager
from game.managers.operation_applier import OperationApplier
from game.options import CardTargetOperationSetChoiceBuilder
from game.actions import UseActionCardAction


class ClasstimeInputManager(InputManagerBase):

    def __init__(self):
        self.action_hand_draw_manager = ActionHandDrawManager()
        self.cto_choice_builder = CardTargetOperationSetChoiceBuilder()
        self.operation_applier = OperationApplier()

    def input(self, current_turn, action):
        assert action.__class__ is UseActionCardAction
        actor = current_turn.actor
        print ("Draw", actor, "CARD:", action.card_id)
        cards = self.action_hand_draw_manager.draw(actor, 1, action.card_id)
        card = cards[0]  
        self.__execute(current_turn, card, action)    
        self._complete_turn(current_turn)
    
    def __execute(self, current_turn, card, action):
        print("    + Executing card {}!".format(card.name))
        card_decisions = action.decisions.get(card.id, {})
        card_target_operation_sets = card.card_target_operation_sets.order_by("execution_order")
        for cto in card_target_operation_sets:
            decision_results = self.cto_choice_builder.build(current_turn, cto, card_decisions, supply_results=True)
            self.operation_applier.apply(decision_results)
