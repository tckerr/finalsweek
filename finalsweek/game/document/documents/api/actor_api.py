from game.scripting.api.base import ProgramChildApi


class ActorApi(ProgramChildApi):

    def list_actors(self):
        for seat in self.data.seats:
            actor = seat.actor
            if actor is not None:
                yield actor

    def list_actors_sorted_by_seat(self):
        actors = list(self.list_actors())
        actors.sort(key=lambda s: (s.seat.row, s.seat.column))
        for actor in actors:
            yield actor

    def get_actor(self, actor_id):
        for actor in self.list_actors():
            if actor.id == actor_id:
                return actor
        raise Exception("Actor not found: {}".format(actor_id))

    def get_action_card_by_actor(self, actor_id, card_id):
        actor = self.get_actor(actor_id)
        for card in actor.action_card_hand.cards:
            if card.id == card_id:
                return card
        raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))

    def expend_action_card(self, actor_id, card_id):
        # TODO: kinda ugly, this line...
        card = self.get_action_card_by_actor(actor_id, card_id)
        actor = self.get_actor(actor_id)
        existing = len(actor.action_card_hand.cards)
        actor.action_card_hand.cards.remove(card)
        if existing == len(actor.action_card_hand.cards):
            raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))
        self.program_api.increment_metadata("expended_action_cards", 1)

    def set_grades(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.grades = value
        actor.grades = max(0, actor.grades)

    def add_grades(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.grades += value
        actor.grades = max(0, actor.grades)

    def set_popularity(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.popularity = value
        actor.popularity = max(0, actor.popularity)

    def add_popularity(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.popularity += value
        actor.popularity = max(0, actor.popularity)

    def set_trouble(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.trouble = value
        actor.trouble = max(0, actor.trouble)

    def add_trouble(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.trouble += value
        actor.trouble = max(0, actor.trouble)

    def set_torment(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.torment = value
        actor.torment = max(0, actor.torment)

    def add_torment(self, actor_id, value):
        actor = self.get_actor(actor_id)
        actor.torment += value
        actor.torment = max(0, actor.torment)