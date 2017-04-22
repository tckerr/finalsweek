from datetime import datetime

from game.document.game_document_cache import GameDocumentCache
from game.document.seed_generators import GameSeedGenerator
from game.gameflow.flowstate.providers import CurrentTurnProvider

'''
    MessageBus --> receive message
    > pass through registered filters
    > call GameApi with final message

'''


class ProgramApi(object):
    """ProgramApi is the primary class through which the internal systems retrieve and modify game state"""

    @classmethod
    def from_id(cls, game_id):
        cache = GameDocumentCache()
        cache.load_from_id(game_id)
        return cls(cache)

    @classmethod
    def new(cls, player_count):
        generator = GameSeedGenerator()
        game_seed = generator.generate(player_count=player_count)
        cache = GameDocumentCache()
        cache.load_from_seed(game_seed)
        return cls(cache)

    def __init__(self, cache):
        self._cache = cache
        self.current_turn_provider = CurrentTurnProvider()

    @property
    def data(self):
        return self._cache.cache

    def save_game(self):
        game_id = self._cache.save()
        return game_id

    def increment_metadata(self, key, value):
        if key not in self.data.metadata:
            self.data.metadata[key] = 0
        self.data.metadata[key] += value

    # TODO: BREAK THESE UP

    # SETTINGS -----------------------------------

    def get_game_definition(self):
        return self.data.rules.game_definition

    def get_hand_size(self):
        return self.data.rules.settings.hand_size

    # STAGES -----------------------------------
    def list_stages(self):
        return self.data.gameflow.stages

    def create_stage(self, stage_type):
        return self.data.gameflow.add_stage(stage_type)

    def complete_stage(self, stage_id):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                stage.completed = datetime.utcnow()
                return

    # PHASES -----------------------------------
    def create_phase(self, stage_id, phase_type):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                return stage.add_phase(phase_type)

    def get_phase_definition(self, phase_type):
        stage_definitions = self.data.rules.game_definition
        for stage_definition in stage_definitions:
            for phase_definition in stage_definition.phases:
                if phase_definition.phase_type == phase_type:
                    return phase_definition

    def complete_phase(self, phase_id):
        for stage in self.data.gameflow.stages:
            for phase in stage.phases:
                if phase.id == phase_id:
                    phase.completed = datetime.utcnow()
                    return

    # TURNS -----------------------------------
    def get_current_turn(self, fresh=False):
        return self.current_turn_provider.get_or_create_turn(self, fresh)

    def create_turn(self, phase_id, actor_id):
        for stage in self.data.gameflow.stages:
            for phase in stage.phases:
                if phase.id == phase_id:
                    return phase.create_turn(actor_id)
        raise Exception("Phase {} not found.".format(phase_id))

    def list_turns(self):
        for stage in self.data.gameflow.stages:
            for phase in stage.phases:
                for turn in phase.turns:
                    yield turn

    def complete_turn(self, turn_id):
        for turn in self.list_turns():
            if turn.id == turn_id:
                return turn.set_complete()
        raise Exception("Turn not found: {}".format(turn_id))

    def refresh_current_turn(self, turn_id):
        turn = self.get_current_turn()
        assert turn.id == turn_id
        turn.refresh()

    # Game decks -----------------------------------

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
            print("    + Drawing {} card, pc: {}".format(card.template.name, card.id))
            drawn.append(card)
        self.increment_metadata("drawn_action_cards", len(drawn))
        return drawn

    # Card Templates -----------------------------------

    def get_card_template(self, card_template_id):
        if card_template_id not in self.data.rules.card_templates:
            raise Exception("Card template not found: {}".format(card_template_id))
        return self.data.rules.card_templates.get(card_template_id)

    # Cards -----------------------------------

    def get_action_card_by_actor(self, actor_id, card_id):
        actor = self.get_actor(actor_id)
        for card in actor.action_card_hand.cards:
            if card.id == card_id:
                return card
        raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))

    # SEATS -----------------------------------
    def list_seats(self):
        return self.data.seats

    def get_seat(self, seat_id):
        for seat in self.list_seats():
            if seat.id == seat_id:
                return seat
        raise Exception("Seat not found: {}".format(seat_id))

    # STUDENTS -----------------------------------
    def list_students(self):
        for seat in self.data.seats:
            student = seat.student
            if student is not None:
                yield student

    def get_student(self, student_id):
        for student in self.list_students():
            if student.id == student_id:
                return student
        raise Exception("Student not found: {}".format(student_id))

    def move_student_to_empty_seat(self, student_id, seat_id):
        seat = self.get_seat(seat_id)
        student = self.get_student(student_id)
        old_seat = student.seat
        assert seat.empty
        seat.student = student
        old_seat.student = None

    def swap_seat(self, student_a_id, seat_b_id):
        student_a = self.get_student(student_a_id)
        seat_a = student_a.seat
        seat_b = self.get_seat(seat_b_id)
        student_b = seat_b.student

        seat_b.student = student_a
        seat_a.student = student_b

    # ACTORS -----------------------------------
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

    def expend_action_card(self, actor_id, card_id):
        card = self.get_action_card_by_actor(actor_id, card_id)
        actor = self.get_actor(actor_id)
        existing = len(actor.action_card_hand.cards)
        actor.action_card_hand.cards.remove(card)
        if existing == len(actor.action_card_hand.cards):
            raise Exception("Card not found: {}, actor id: {}".format(card_id, actor_id))
        self.increment_metadata("expended_action_cards", 1)

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


