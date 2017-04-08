from game.actions import DrawAction
from game.managers.input.input_manager_base import InputManagerBase
from game.managers.draw_manager import DeckDrawManager

class AccumulationInputManager(InputManagerBase):

    def __init__(self):
        self.__deck_draw_manager = DeckDrawManager()

    def input(self, turn, action):
        assert action.__class__ is DrawAction
        actor = turn.actor
        hand = actor.action_hand
        deck = actor.game.action_deck
        quantity = action.quantity
        self.__deck_draw_manager.draw(from_pile=deck, to_pile=hand, quantity=quantity)
        self._complete_turn(turn)