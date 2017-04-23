from game.operation.operator_eligible import receives_operation
from game.scripting.api.program_child_api import ProgramChildApi


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

    @receives_operation
    def list_actors(self):
        return self._actors()

    @receives_operation
    def list_actors_sorted_by_seat(self):
        actors = list(self._actors())
        actors.sort(key=lambda s: (s.seat.row, s.seat.column))
        for actor in actors:
            yield actor

    @receives_operation
    def get_actor(self, actor_id):
        return self._actor(actor_id)

    @receives_operation
    def get_action_card_by_actor(self, actor_id, card_id):
        return self._action_card_by_actor(actor_id, card_id)

    @receives_operation
    def expend_action_card(self, actor_id, card_id):
        # TODO: kinda ugly, this line...
        card = self._action_card_by_actor(actor_id, card_id)
        actor = self._actor(actor_id)
        existing = len(actor.action_card_hand.cards)
        actor.action_card_hand.cards.remove(card)
        if existing == len(actor.action_card_hand.cards):
            raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))
        self.program_api.increment_metadata("expended_action_cards", 1)

    @receives_operation
    def set_grades(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.grades = value
        actor.grades = max(0, actor.grades)

    @receives_operation
    def add_grades(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.grades += value
        actor.grades = max(0, actor.grades)

    @receives_operation
    def set_popularity(self, actor_id, value):
        actor = self._actor(actor_id)
        actor.popularity = value
        actor.popularity = max(0, actor.popularity)

    @receives_operation
    def add_popularity(self, actor_id, value):
        actor = self._actor(actor_id)
        actor.popularity += value
        actor.popularity = max(0, actor.popularity)

    @receives_operation
    def set_trouble(self, actor_id, value):
        actor = self._actor(actor_id)
        actor.trouble = value
        actor.trouble = max(0, actor.trouble)

    @receives_operation
    def add_trouble(self, actor_id, value):
        actor = self._actor(actor_id)
        actor.trouble += value
        actor.trouble = max(0, actor.trouble)

    @receives_operation
    def set_torment(self, actor_id, value):
        actor = self._actor(actor_id)
        actor.torment = value
        actor.torment = max(0, actor.torment)

    @receives_operation
    def add_torment(self, actor_id, value):
        actor = self._actor(actor_id)
        actor.torment += value
        actor.torment = max(0, actor.torment)
