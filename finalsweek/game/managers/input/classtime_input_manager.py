from game.managers.input.input_manager_base import InputManagerBase
from game.managers.draw_manager import ActionHandDrawManager
from game.actions import UseActionCardAction

class ClasstimeInputManager(InputManagerBase):

    def __init__(self):
        self.action_hand_draw_manager = ActionHandDrawManager()

    def input(self, turn, action):
        assert action.__class__ is UseActionCardAction
        actor = turn.actor
        cards = self.action_hand_draw_manager.draw(actor, 1, action.card_id)
        card = cards[0]  
        self.__execute(actor, card)    
        self._complete_turn(turn)
    
    def __execute(self, actor, card):
        print("      (Doing something significant with card {}!)".format(card.name))
        
