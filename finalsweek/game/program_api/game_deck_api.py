from game.configuration.definitions import LogLevel, LogType, OperationType, OperatorType
from game.operation.decorators import accepts_operation, accepts_operator
from game.scripting.api.program_child_api import ProgramChildApi
from logger import Logger


class GameDeckApi(ProgramChildApi):

    @accepts_operation(OperationType.Draw)
    @accepts_operator(OperatorType.Add)
    def draw_action_cards(self, operation):
        operation = self._mutate(operation)
        actor = self.program_api.actors.get(operation.targeted_actor_id)
        action_card_deck = self.data.action_card_deck
        self._assert_deck_size(action_card_deck, operation.value)
        drawn = [self._draw_card(action_card_deck, actor) for _ in range(0, operation.value)]
        self.program_api.increment_metadata("drawn_action_cards", len(drawn))
        return drawn

    def _draw_card(self, action_card_deck, actor):
        card = action_card_deck.cards.pop()
        actor.action_card_hand.cards.append(card)
        self._log_card_draw(card)
        return card

    @staticmethod
    def _assert_deck_size(action_card_deck, quantity):
        deck_length = len(action_card_deck.cards)
        if deck_length < quantity:
            message = "Cannot draw {quantity} cards from a pile of size {pile_size}."
            raise Exception(message.format(quantity=quantity, pile_size=deck_length))

    @staticmethod
    def _log_card_draw(card):
        message = "Drawing {} card, pc: {}".format(card.template.name, card.id)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
