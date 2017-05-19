from game.definitions import OperatorType, Tag
from game.operation.operations.draw import Draw


class DrawManager(object):
    @staticmethod
    def refill_hand(actor, api):
        hand_size = api.settings.get_hand_size()
        hand = actor.action_card_hand
        cards_needed = max(0, hand_size - len(hand.cards))
        operation = Draw(
            operator=OperatorType.Add,
            value=cards_needed,
            targeted_actor_id=actor.id,
            tags={Tag.Draw, Tag.DrawActionCard}
        )
        api.game_decks.draw_action_cards(operation=operation)

