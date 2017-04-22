class HandRefiller(object):

    @staticmethod
    def refill_hand(actor, api):
        hand_size = api.settings.get_hand_size()
        hand = actor.action_card_hand
        cards_needed = max(0, hand_size - len(hand.cards))
        api.game_decks.draw_action_cards(actor, cards_needed)


