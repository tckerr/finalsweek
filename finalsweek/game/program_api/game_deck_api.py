from game.scripting.api.program_child_api import ProgramChildApi
from logger import log


class GameDeckApi(ProgramChildApi):
    def draw_action_cards(self, actor, quantity):
        # TODO: extract logic
        action_card_deck = self.data.action_card_deck
        deck_length = len(action_card_deck.cards)
        if deck_length < quantity:
            raise Exception(
                "Cannot draw {quantity} cards from a pile of size {pile_size}.".format(quantity=quantity,
                                                                                       pile_size=deck_length))
        drawn = []
        for _ in range(0, quantity):
            card = action_card_deck.cards.pop()
            actor.action_card_hand.cards.append(card)
            log("    + Drawing {} card, pc: {}".format(card.template.name, card.id))
            drawn.append(card)
        self.program_api.increment_metadata("drawn_action_cards", len(drawn))
        return drawn
