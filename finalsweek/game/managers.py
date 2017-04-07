from game.models import PileCard
from game.actions import DrawAction
from django.utils import timezone
from random import shuffle

class InputManagerBase(object):
    def _complete_turn(self, turn):
        turn.completed=timezone.now()
        turn.save()

class InputManager(InputManagerBase):

    def __init__(self):
        self.phase_type_managers = {
            "Accumulation": AccumulationInputManager()
        }

    def input(self, turn, action):
        phase_type_id = turn.phase.phase_type_id
        if phase_type_id in self.phase_type_managers:
            return self.phase_type_managers[phase_type_id].input(turn, action)
        else:
            # temporary until i build em all
            self._complete_turn(turn)


class AccumulationInputManager(InputManagerBase):

    def input(self, turn, action):
        assert action.__class__ is DrawAction
        pile_cards = list(turn.actor.game.action_deck.get_cards())
        shuffle(pile_cards)
        self.__draw(pile_cards, action.count, turn.actor.action_hand)
        self._complete_turn(turn)

    def __draw(self, deck, quantity, hand):
        for draw in range(0, quantity):
            pile_card = deck.pop()
            pile_card.pile = hand
            print("    + Drawing {} card".format(pile_card.card.name))
            pile_card.save()

        
