from game.models import Pile, Actor, Game, StudentInfo, Card, Seat
from game.settings import settings
from random import shuffle
from django.db import transaction

class ActionDeckFactory(object):

    def __init__(self):
        self.pile_factory = PileFactory()

    def create(self, size_limit):
        pile = self.pile_factory.create(size_limit)
        active_cards = list(Card.objects.filter(active=True))
        cards_per_type = int(settings["total_cards"]/len(active_cards))
        for card in active_cards:
            for _ in range(0, cards_per_type):
                pile.add_card(card)
        return pile

class PileFactory(object):

    def create(self, size_limit):
        pile = Pile()
        pile.size_limit = size_limit
        pile.save()
        return pile

class ActorFactory(object):
    def __init__(self):
        self.pile_factory = PileFactory()

    def create(self, game, seat):            
        actor = Actor()
        actor.game = game
        actor.grades = 0
        actor.popularity = 0
        actor.trouble = 0
        actor.torment = 0
        actor.seat = seat
        actor.student_info = StudentInfo.objects.get(name="Test Student")
        actor.discard_pile = self.__create_pile(None)
        actor.afterschool_hand = self.__create_pile(None)
        actor.action_hand = self.__create_pile(settings["hand_size"])
        actor.save()

    def load(self, actor_id, prefetch=None):
        base_qs = Actor.objects
        if prefetch:
            return base_qs.prefetch_related(prefetch).get(id=actor_id)
        return base_qs.get(id=actor_id)  

    def __create_pile(self, size_limit):
        pile = Pile()
        pile.size_limit = size_limit
        pile.save()
        return pile

class SeatFactory(object):

    def create(self, game, row, column):            
        seat = Seat()
        seat.game = game
        seat.row = row
        seat.column = column
        seat.save()
        return seat

    def create_for_grid(self, game, row_dims, column_dims):
        seats = []
        for row in range(0, row_dims):
            for column in range(0, column_dims):
                seats.append(self.create(game, row, column))
        return seats

class GameFactory(object):

    def __init__(self):
        self.actor_factory = ActorFactory()
        self.pile_factory = PileFactory()
        self.action_deck_factory = ActionDeckFactory()
        self.seat_factory = SeatFactory()

    def load(self, game_id):
        return Game.objects.get(id=game_id)  

    def create(self, ai_players):   
        with transaction.atomic():         
            game = Game()
            game.action_deck = self.action_deck_factory.create(None)
            game.afterschool_deck = self.pile_factory.create(None)
            game.discipline_card_deck = self.pile_factory.create(None)
            game.save()
            self.seat_factory.create_for_grid(game, settings["seat_rows"], settings["seat_columns"])
            self.__create_actors_with_seat(game, ai_players)
            return game

    def __create_actors_with_seat(self, game, ai_players):
        seats = list(game.seats.all())
        shuffle(seats)
        for _ in range(0, ai_players):
            seat = seats.pop()
            self.actor_factory.create(game, seat)
