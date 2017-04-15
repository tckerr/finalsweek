from game.managers.input.input_manager_base import InputManagerBase
from game.managers.draw_manager import ActionHandDrawManager
from game.managers.operation_applier import OperationApplier
from game.options import CardTargetOperationSetChoiceBuilder
from game.actions import UseActionCardAction
from game.models import Card, PileCard
from game.script_api import TrustedScriptRunner


class ClasstimeInputManager(InputManagerBase):

    def __init__(self):
        self.action_hand_draw_manager = ActionHandDrawManager()
        self.cto_choice_builder = CardTargetOperationSetChoiceBuilder()
        self.operation_applier = OperationApplier()
        self.trusted_script_runner = TrustedScriptRunner()

    def input(self, current_turn, action):
        assert action.__class__ is UseActionCardAction
        actor = current_turn.actor
        pc = PileCard.objects.prefetch_related("card").get(pk=action.pc_id, pile_id=actor.action_hand.id)
        prompt = self.__execute(current_turn, pc.card, actor, action.decisions) 
        if prompt:
            return prompt
        print ("Draw", actor, "CARD:", pc.card.name)
        self.action_hand_draw_manager.draw_pc(actor, pc)
        self._complete_turn(current_turn)
    
    def __execute(self, current_turn, card, actor, decisions):
        print("    + Executing card {}!".format(card.name))
        script = card.script
        return self.trusted_script_runner.run(actor, script, decisions)

