from random import shuffle
from game.models import PileCard


class DrawManager(object):

    def draw(self, from_pile, to_pile, quantity, card_id=None):
        pilecards = self._get_pilecards(from_pile, card_id)
        return self._transfer(pilecards, to_pile, quantity)

    def _get_pilecards(self, from_pile, card_id=None):

        pilecards = list(PileCard.objects.filter(pile=from_pile))
        if card_id:
            return list(filter(lambda pc: pc.card_id == card_id, pilecards))
        return pilecards

    def _transfer(self, pilecards, to_pile, quantity):
        if len(pilecards) <= quantity:
            raise Exception("Cannot draw {quantity} cards from a pile of size {pilesize}.".format(quantity=str(quantity), pilesize=str(len(pilecards))))
        cards = []
        for carddraw in range(0, quantity):
            pilecard = pilecards.pop()
            pilecard.pile = to_pile
            print("    + Drawing {} card, pc: {}".format(pilecard.card.name, str(pilecard.id)))
            pilecard.save()
            cards.append(pilecard.card)
        return cards

class DeckDrawManager(DrawManager):

    def draw(self, from_pile, to_pile, quantity):
        pilecards = self._get_pilecards(from_pile)
        shuffle(pilecards)
        return self._transfer(pilecards, to_pile, quantity)


class ActionHandDrawManager(DrawManager):

    def draw(self, actor, quantity, card_id):
        to_pile = actor.discard_pile
        from_pile = actor.action_hand
        pilecards = self._get_pilecards(from_pile, card_id) 
        return self._transfer(pilecards, to_pile, quantity)