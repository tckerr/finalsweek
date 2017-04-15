from game.actions import DrawAction
from game.managers.input.input_manager_base import InputManagerBase
from game.managers.draw_manager import DeckDrawManager

class AccumulationInputManager(InputManagerBase):

    def __init__(self):
        self.__deck_draw_manager = DeckDrawManager()

    def input(self, turn, action):
        self._complete_turn(turn)