from datetime import datetime
#
from sim.exceptions import NotImplementedException, RulesViolation
from sim.messaging.message_types import MessageTypes
from sim.messaging.message_dispatcher import MessageDispatcher#
from sim.engine.game import Game
from sim.engine.ruleset import Ruleset
from sim.engine.systems.gameslot_manager import GameslotManager
from sim.engine.systems.turn_manager import TurnManager
from sim.entity.providers import ComponentEntityMap
from sim.entity.factories.actor_factory import ActorFactory
from sim.entity.entity import Entity

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
        game_manager.initialize_gamestate()
        return game_manager
   

class GameManager(object):

    def __init__(self, game):
        self.game = game
        self.message_dispatcher = MessageDispatcher(self.game.id)      
        self.gameslot_manager = GameslotManager(self.game) 
        self.turn_manager = TurnManager(self.game) 

    @property
    def game_id(self):
        return self.game.id

    def initialize_gamestate(self):
        self.gameslot_manager.jumble()
        self.turn_manager.provide_turn()    

    def expend_action(self, entity_id, cost):        
        entity = Entity.objects.get(pk=entity_id)
        self.turn_manager.expend_action(entity, cost)
        self.__provide_turn()

    def __provide_turn(self):
        self.turn_manager.provide_turn()