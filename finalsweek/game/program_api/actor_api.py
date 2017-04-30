from game.configuration.definitions import OperationType, OperatorType, LogLevel, LogType
from game.document.documents.in_play_effect import InPlayEffect
from game.operation.decorators import accepts_operation, accepts_operator
from game.scripting.api.program_child_api import ProgramChildApi
from game.systems.draw_manager import DrawManager
from logger import Logger
from util.helpers import floor_at_zero
from util.random import random_id


class ActorApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.draw_manager = DrawManager()

    def _get(self, actor_id):
        for actor in self._actors():
            if actor.id == actor_id:
                return actor
        raise Exception("Actor not found: {}".format(actor_id))

    def _actors(self):
        for seat in self.data.seats:
            actor = seat.actor
            if actor is not None:
                yield actor

    def _get_targeted_actor(self, operation):
        return self.get(operation.targeted_actor_id)

    def _action_card_by_actor(self, actor_id, card_id):
        actor = self.get(actor_id)
        for card in actor.action_card_hand.cards:
            if card.id == card_id:
                return card
        message = "Card not found: {}, actor id: {}".format(card_id, actor_id)
        message_warning = "Ensure card was moved to inPlay ({})".format(
            [c.card.id for c in actor.cards_in_play])
        Logger.log("WARNING:", message, message_warning, level=LogLevel.Warning, log_type=LogType.IndexError)
        # raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))

    def list(self):
        return self._actors()

    def list_actors_sorted_by_seat(self):
        actors = list(self._actors())
        actors.sort(key=lambda s: (s.seat.row, s.seat.column))
        for actor in actors:
            yield actor

    def get(self, actor_id):
        return self._get(actor_id)

    def get_action_card_by_actor(self, actor_id, card_id):
        return self._action_card_by_actor(actor_id, card_id)

    # TODO: make these fn's system operations

    def expend_action_card(self, actor_id, card_id):
        # TODO: kinda ugly, this line...
        card = self._action_card_by_actor(actor_id, card_id)
        actor = self._get(actor_id)
        # TODO: discard
        try:
            actor.action_card_hand.cards.remove(card)
        except ValueError:
            message = "Card not found: {}, actor id: {}".format(card_id, actor_id)
            Logger.log(message, level=LogLevel.Error, log_type=LogType.IndexError)
        self.program_api.increment_metadata("expended_action_cards", 1)

    # TODO: system operation
    # TODO: make an in_play API

    def transfer_card_to_in_play(self, source_actor_id, targeted_actor_id, card_id, mutation_id):
        card = self._action_card_by_actor(source_actor_id, card_id)
        source_actor = self._get(source_actor_id)
        source_actor.action_card_hand.cards.remove(card)
        target_actor = source_actor if source_actor_id == targeted_actor_id else self._get(targeted_actor_id)
        # todo: move to factory
        in_play_effect_seed = {
            "id":          random_id(),
            "mutation_id": mutation_id,
            "card":        card
        }
        in_play_effect = InPlayEffect(in_play_effect_seed, target_actor)
        target_actor.cards_in_play.append(in_play_effect)

    def remove_mutation_and_card_in_play(self, mutation_id):
        self.program_api.mutations.remove_mutation(mutation_id)
        card_to_remove = None
        for actor in self._actors():
            for card_in_play in actor.cards_in_play:
                if card_in_play.mutation_id == mutation_id:
                    card_to_remove = card_in_play
                    break
            if card_to_remove is not None:
                actor.cards_in_play.remove(card_to_remove)
                message = "Removed mutation {} from play".format(mutation_id)
                Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
            return

    def get_by_mutation(self, mutation_id):
        for actor in self._actors():
            for card_in_play in actor.cards_in_play:
                if card_in_play.mutation_id == mutation_id:
                    return actor

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_grades(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.grades = floor_at_zero(operation.value)
        self._log_mod_operation(actor, "grades", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_grades(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.grades = floor_at_zero(actor.grades + operation.value)
        self._log_mod_operation(actor, "grades", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_popularity(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.popularity = floor_at_zero(operation.value)
        self._log_mod_operation(actor, "popularity", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_popularity(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.popularity = floor_at_zero(actor.popularity + operation.value)
        self._log_mod_operation(actor, "popularity", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_trouble(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.trouble = floor_at_zero(operation.value)
        self._log_mod_operation(actor, "trouble", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_trouble(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.trouble = floor_at_zero(actor.trouble + operation.value)
        self._log_mod_operation(actor, "trouble", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_torment(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.torment = floor_at_zero(operation.value)
        self._log_mod_operation(actor, "torment", operation)
        return operation

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_torment(self, operation):
        operation = self._mutate(operation)
        actor = self._get_targeted_actor(operation)
        actor.torment = floor_at_zero(actor.torment + operation.value)
        self._log_mod_operation(actor, "torment", operation)
        return operation

    def refresh_hand(self, actor_id):
        actor = self._get(actor_id)
        # TODO: actual discard effect
        actor.action_card_hand.cards.clear()
        self._log_refresh_hand(actor)
        self.draw_manager.refill_hand(actor, self.program_api)

    @staticmethod
    def _log_mod_operation(actor, stat, operation):
        template = "Modified actor {actor} '{stat}' via '{operator}' with value of '{value}'. Now is: {current_value}"
        Logger.log(template.format(
            actor=actor.label,
            stat=stat,
            operator=operation.operator,
            value=operation.value,
            current_value=getattr(actor, stat)
        ), level=LogLevel.Debug, log_type=LogType.Operational)

    @staticmethod
    def _log_refresh_hand(actor):
        template = "Actor {actor} is refilling hand."
        Logger.log(template.format(actor=actor.label), level=LogLevel.Debug, log_type=LogType.Operational)
