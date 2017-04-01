from datetime import datetime
#
from sim.exceptions import NotImplementedException, RulesViolation
from sim.messaging.message_types import MessageTypes
from sim.messaging.message_dispatcher import MessageDispatcher#
from sim.engine.game import Game
from sim.engine.systems.seat_manager import SeatManager
from sim.entity.providers import ComponentEntityMap
from sim.entity.factories.actor_factory import ActorFactory
from sim.entity.components import (
    Component, 
    GradesComponent, 
    PopularityComponent, 
    TurnComponent,
)
       

class Initializer(object):

    @classmethod
    def new(cls, user_ids, total_actors):
        # pass user ids in as ordered clockwise list from seat 1
        game = Game()
        game.total_actors = total_actors
        game.save()        
        instance = cls(game)
        instance.initialize_players(game.id, user_ids)
        instance.initialize_seats()
        return instance

    @classmethod
    def load(cls, game_id):
        #load here
        game = Game.objects.get(pk=game_id)
        return cls(game)

    def __init__(self, game):
        self.game = game
        self.component_entity_map = ComponentEntityMap(self.game.id)        
        self.message_dispatcher = MessageDispatcher(self.component_entity_map)      
        self.seat_manager = SeatManager(self.component_entity_map, self.game) 
        self.actor_factory = ActorFactory(self.component_entity_map)

    def initialize_players(self, game_id, user_ids):
        if len(user_ids) > self.game.total_actors:
            raise RulesViolation()
        remaining = self.game.total_actors        
        for user_id in user_ids:
            remaining -= 1
            self.actor_factory.create_user(game_id, user_id)
        if self.game.auto_create_ai:
            for ai in range(0, remaining):
                self.actor_factory.create_ai(game_id)

    def initialize_seats(self):
        self.seat_manager.jumble()

    # ---- DEBUGGING ----

    def mock(self):
        messages = (
            ( MessageTypes.GradesModification, {"value": 15, "target_entity_id": 1} ),
            ( MessageTypes.ReportGrades, ),
            ( MessageTypes.DebugValues, ),
        )

        for message in messages:
            self.message_dispatcher.dispatch(*message)

    def performance_test(self):
        start = datetime.now()        
        mock_message = ( MessageTypes.DebugValues, {"value": "hello world"} )
        self.message_dispatcher.dispatch(*mock_message)
        end = datetime.now()
        elapsed = end - start
        print("Time to dispatch 1 message to {} entities:".format(str(self.game.total_actors)), elapsed.total_seconds())
        
