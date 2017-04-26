from game.operation.decorators import accepts_operation, accepts_operator
from game.operation.operation import OperationType, OperatorType
from game.scripting.api.program_child_api import ProgramChildApi
from util import floor_at_zero


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

    def _action_card_by_actor(self, actor_id, card_id):
        actor = self.get_actor(actor_id)
        for card in actor.action_card_hand.cards:
            if card.id == card_id:
                return card
        raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))

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

    def expend_action_card(self, actor_id, card_id):
        # TODO: kinda ugly, this line...
        card = self._action_card_by_actor(actor_id, card_id)
        actor = self._actor(actor_id)
        existing = len(actor.action_card_hand.cards)
        actor.action_card_hand.cards.remove(card)
        if existing == len(actor.action_card_hand.cards):
            raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))
        self.program_api.increment_metadata("expended_action_cards", 1)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_grades(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.grades = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_grades(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.grades = floor_at_zero(actor.grades + operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_popularity(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.popularity = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_popularity(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.popularity = floor_at_zero(actor.popularity + operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_trouble(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.trouble = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_trouble(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.trouble = floor_at_zero(actor.trouble + operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Set)
    def set_torment(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.torment = floor_at_zero(operation.value)

    @accepts_operation(OperationType.ModifyAttribute)
    @accepts_operator(OperatorType.Add)
    def add_torment(self, operation):
        operation = self._mutate(operation)
        actor = self.get_actor(operation.actor_id)
        actor.torment = floor_at_zero(actor.torment + operation.value)
