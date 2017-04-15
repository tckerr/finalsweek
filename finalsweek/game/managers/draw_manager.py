from random import shuffle
from game.models import PileCard
from game.settings import settings

class HandRefiller(object):
    def __init__(self):
        self.__deck_draw_manager = DeckDrawManager()

    def refill_hand(self, actor):
        hand = actor.action_hand
        cards_needed = max(0, settings["hand_size"] - hand.pile_cards.count())
        if cards_needed > 0:            
            deck = actor.game.action_deck
            self.__deck_draw_manager.draw(from_pile=deck, to_pile=hand, quantity=cards_needed)

class DrawManager(object):

    def draw(self, from_pile, to_pile, quantity, card_id=None):
        pilecards = self._get_pilecards(from_pile, card_id)
        return self._transfer(pilecards, to_pile, quantity)

    def _get_pilecards(self, from_pile, card_id=None):

        pilecards = list(PileCard.objects.filter(pile=from_pile).prefetch_related("card"))
        if card_id:
            return list(filter(lambda pc: pc.card_id == card_id, pilecards))
        return pilecards

    def _transfer(self, pilecards, to_pile, quantity):
        if len(pilecards) < quantity:
            raise Exception("Cannot draw {quantity} cards from a pile of size {pilesize}.".format(quantity=str(quantity), pilesize=str(len(pilecards))))
        drawn = []
        for carddraw in range(0, quantity):
            pilecard = pilecards.pop()
            pilecard.pile = to_pile
            print("    + Drawing {} card, pc: {}".format(pilecard.card.name, str(pilecard.id)))            
            drawn.append(pilecard)
        PileCard.objects.filter(pk__in=[pc.id for pc in drawn]).update(pile=to_pile)
        return [pc.card for pc in drawn]
        

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

    def draw_pc(self, actor, pc):
        to_pile = actor.discard_pile
        from_pile = actor.action_hand        
        return self._transfer([pc], to_pile, 1)