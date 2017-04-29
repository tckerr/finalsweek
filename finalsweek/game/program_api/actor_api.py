from game.document.documents.in_play_effect import InPlayEffect
from game.operation.decorators import accepts_operation, accepts_operator
from game.configuration.definitions import OperationType, OperatorType
from game.scripting.api.program_child_api import ProgramChildApi
from logger import log
from util import floor_at_zero, guid


class ActorApi(ProgramChildApi):
    def _actor(self, actor_id):
        for actor in self._actors():
            if actor.id == actor_id:
                return actor
        raise Exception("Actor not found: {}".format(actor_id))

    def _actors(self):
        for seat in self.data.seats:
            actor = seat.actor
            if actor is not None:
                yield actor

    def _operation_targeted_actor(self, operation):
        return self.get_actor(operation.targeted_actor_id)

    def _action_card_by_actor(self, actor_id, card_id):
        actor = self.get_actor(actor_id)
        for card in actor.action_card_hand.cards:
            if card.id == card_id:
                return card
        message = "Card not found: {}, actor id: {}".format(card_id, actor_id)
        message_warning = "Ensure card was moved to inPlay ({})".format(
            [c.card.id for c in actor.cards_in_play])
        print("WARNING:", message, message_warning)
        # raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))

    def list_actors(self):
        return self._actors()

    def list_actors_sorted_by_seat(self):
        actors = list(self._actors())
        actors.sort(key=lambda s: (s.seat.row, s.seat.column))
        for actor in actors:
            yield actor

    def get_actor(self, actor_id):
        return self._actor(actor_id)

    def get_action_card_by_actor(self, actor_id, card_id):
        return self._action_card_by_actor(actor_id, card_id)

    # TODO: system operation

    def expend_action_card(self, actor_id, card_id):
        # TODO: kinda ugly, this line...
        card = self._action_card_by_actor(actor_id, card_id)
        actor = self._actor(actor_id)
        # TODO: discard
        try:
            actor.action_card_hand.cards.remove(card)
        except ValueError:
            message = "Card not found: {}, actor id: {}".format(card_id, actor_id)
            raise Exception(message)
        self.program_api.increment_metadata("expended_action_cards", 1)

    # TODO: system operation

    def transfer_card_to_in_play(self, actor_id, card_id, mutation_id):
        card = self._action_card_by_actor(actor_id, card_id)
        actor = self._actor(actor_id)
        actor.action_card_hand.cards.remove(card)
        # todo: move to factory
        in_play_effect_seed = {
            "id":          guid(),
            "mutation_id": mutation_id,
            "card":        card
        }
        in_play_effect = InPlayEffect(in_play_effect_seed, actor)
        actor.cards_in_play.append(in_play_effect)

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
                log("Removed mutation from play...")
            return

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_grades(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.grades = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_grades(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.grades = floor_at_zero(actor.grades + operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_popularity(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.popularity = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_popularity(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.popularity = floor_at_zero(actor.popularity + operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_trouble(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.trouble = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_trouble(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.trouble = floor_at_zero(actor.trouble + operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_torment(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.torment = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_torment(self, operation):
        operation = self._mutate(operation)
        actor = self._operation_targeted_actor(operation)
        actor.torment = floor_at_zero(actor.torment + operation.value)
