from game.models import Pile, Actor, Game, StudentInfo, Card
from game.settings import settings

class ActionDeckFactory(object):

    def __init__(self):
        self.pile_factory = PileFactory()

    def create(self, size_limit):
        pile = self.pile_factory.create(size_limit)
        for card in Card.objects.all():
            for _ in range(0, settings["card_copies_in_action_deck"]):
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

    def create(self, game):            
        actor = Actor()
        actor.game = game
        actor.grades = 0
        actor.popularity = 0
        actor.student_info = StudentInfo.objects.get(name="Test Student")
        actor.discard_pile = self.__create_pile(None)
        actor.afterschool_hand = self.__create_pile(None)
        actor.action_hand = self.__create_pile(settings["hand_size"])
        actor.save()

    def load(self, actor_id):
        return Actor.objects.get(id=actor_id)  

    def __create_pile(self, size_limit):
        pile = Pile()
        pile.size_limit = size_limit
        pile.save()
        return pile

class GameFactory(object):

    def __init__(self):
        self.actor_factory = ActorFactory()
        self.pile_factory = PileFactory()
        self.action_deck_factory = ActionDeckFactory()

    def load(self, game_id):
        return Game.objects.get(id=game_id)  

    def create(self, ai_players):            
        game = Game()
        game.play_phase_count = settings["play_phase_count"]
        game.action_deck = self.action_deck_factory.create(None)
        game.afterschool_deck = self.pile_factory.create(None)
        game.discipline_card_deck = self.pile_factory.create(None)
        game.save()
        for _ in range(0, ai_players):
            self.actor_factory.create(game)
        return game
