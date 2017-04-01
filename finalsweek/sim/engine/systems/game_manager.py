from datetime import datetime
#
from sim.exceptions import NotImplementedException, RulesViolation
from sim.messaging.message_types import MessageTypes
from sim.messaging.message_dispatcher import MessageDispatcher#
from sim.engine.game import Game
from sim.engine.ruleset import Ruleset
from sim.engine.systems.seat_manager import SeatManager
from sim.engine.systems.turn_manager import TurnManager
from sim.entity.providers import ComponentEntityMap
from sim.entity.factories.actor_factory import ActorFactory


class GameManagerFactory(object):

    def __init__(self):
        self.actor_factory = ActorFactory()

    def load(self, game_id):
        game = Game.objects.get(pk=game_id)
        return GameManager(game)

    def create_new(self, user_ids, ai_slots, ruleset_id):

        ruleset = Ruleset.objects.get(pk=ruleset_id)

        if ai_slots > 0 and not ruleset.auto_create_ai:
            raise RulesViolation("You cannot create AI if it isn't permitted in the rules.")

        if len(user_ids) + ai_slots > ruleset.max_actors:
            raise RulesViolation("You have more actors than open spots.")        

        game = self.__create_new_game(ruleset)
        self.__initialize_players(game.id, user_ids, ai_slots)
        game_manager = self.__initialize_game_manager(game, user_ids)
        return game_manager

    def __create_new_game(self, ruleset):
        game = Game()
        game.ruleset = ruleset
        game.save()  
        return game

    def __initialize_players(self, game_id, user_ids, ai_slots):
        for user_id in user_ids:
            self.actor_factory.create_user(game_id, user_id)
        for ai_slot in range(0, ai_slots):
            self.actor_factory.create_ai(game_id)

    def __initialize_game_manager(self, game, user_ids):
        game_manager = GameManager(game)
        game_manager.jumble_seats()
        game_manager.initialize_turns()
        return game_manager
   

class GameManager(object):

    def __init__(self, game):
        self.game = game
        self.message_dispatcher = MessageDispatcher(self.game.id)      
        self.seat_manager = SeatManager(self.game) 
        self.turn_manager = TurnManager(self.game) 

    @property
    def game_id(self):
        return self.game.id

    def jumble_seats(self):
        self.seat_manager.jumble()

    def initialize_turns(self):
        if self.turn_manager.needs_turn_assignment():
            self.turn_manager.initialize_next_turn()
