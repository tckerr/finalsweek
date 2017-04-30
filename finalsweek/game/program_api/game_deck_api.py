from game.configuration.definitions import LogLevel, LogType, OperationType, OperatorType
from game.operation.decorators import accepts_operation, accepts_operator
from game.scripting.api.program_child_api import ProgramChildApi
from logger import Logger


# TODO: split action card and dismissal card APIs
class GameDeckApi(ProgramChildApi):
    @accepts_operation(OperationType.Draw)
    @accepts_operator(OperatorType.Add)
    def draw_action_cards(self, operation):
        operation = self._mutate(operation)
        actor = self.program_api.actors.get(operation.targeted_actor_id)
        action_card_deck = self.data.action_card_deck
        self._assert_deck_size(action_card_deck, operation.value)
        drawn = [self._draw_action_card(action_card_deck, actor) for _ in range(0, operation.value)]
        self.program_api.increment_metadata("drawn_action_cards", len(drawn))
        return drawn

    def set_discipline_card_for_phase(self, phase):
        discipline_card = self.data.discipline_card_deck.cards.pop()
        self.data.phase_discipline_cards[phase.id] = discipline_card
        self._log_discipline_card_draw(discipline_card, phase.phase_type)
        return discipline_card

    def _draw_action_card(self, action_card_deck, actor):
        card = action_card_deck.cards.pop()
        actor.action_card_hand.cards.append(card)
        self._log_action_card_draw(card)
        return card

    @staticmethod
    def _assert_deck_size(action_card_deck, quantity):
        deck_length = len(action_card_deck.cards)
        if deck_length < quantity:
            message = "Cannot draw {quantity} cards from a pile of size {pile_size}."
            raise Exception(message.format(quantity=quantity, pile_size=deck_length))

    @staticmethod
    def _log_action_card_draw(card):
        message = "Drew action card '{}', pc: {}".format(card.template.name, card.id)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)

    @staticmethod
    def _log_discipline_card_draw(discipline_card, phase_type):
        message = "Drew dismissal card '{}' for phase '{}'".format(discipline_card.template.name, phase_type)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
