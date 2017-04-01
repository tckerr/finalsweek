from datetime import datetime
#
from sim.exceptions import NotImplementedException, RulesViolation
from sim.messaging.message_types import MessageTypes
from sim.messaging.message_dispatcher import MessageDispatcher#
from sim.engine.systems.seat_manager import SeatManager
from sim.entity.providers import ComponentEntityMap
from sim.entity.factories.actor_factory import ActorFactory
from sim.entity.components import (
    Component, 
    GradesComponent, 
    PopularityComponent, 
    TurnComponent,
)


class InitializationState(object):
    "Post data for new game"
    def __init__(self, user_ids):
        self.user_ids = user_ids
        

class Initializer(object):

    @classmethod
    def new(cls, user_ids, rules):
        # pass user ids in as ordered clockwise list from seat 1
        instance = cls(ComponentEntityMap(), rules)
        instance.initialize_players(user_ids)
        instance.initialize_seats()
        return instance

    @classmethod
    def load(cls, component_entity_map):
        #load here
        raise NotImplementedException()

    def __init__(self, component_entity_map, rules):
        self.rules = rules
        self.component_entity_map = component_entity_map        
        self.message_dispatcher = MessageDispatcher(self.component_entity_map)      
        self.seat_manager = SeatManager(self.component_entity_map, self.rules) 

    def initialize_players(self, user_ids):
        if len(user_ids) > self.rules.total_actors:
            raise RulesViolation()
        actor_factory = ActorFactory(self.component_entity_map)
        remaining = self.rules.total_actors        
        for user_id in user_ids:
            remaining -= 1
            actor_factory.create_user(user_id)
        if self.rules.auto_create_ai:
            for ai in range(0, remaining):
                actor_factory.create_ai()

    def initialize_seats(self):
        self.seat_manager.jumble()


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
        print("Time to dispatch 1 message to {} entities:".format(str(self.rules.total_actors)), elapsed.total_seconds())
        
