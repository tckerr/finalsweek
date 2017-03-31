from datetime import datetime
#
from sim.messaging.message_types import MessageTypes
from sim.messaging.message_dispatcher import MessageDispatcher
#
from sim.entity.templates import PlayerComponentSetTemplate
from sim.entity.providers import (
    EntityFactory, 
    ComponentEntityMap,
)
from sim.entity.components import (
    Component, 
    GradesComponent, 
    PopularityComponent, 
    TurnComponent,
)

class Initializer(object):

    def __init__(self):
        self.component_entity_map = ComponentEntityMap()
        self.message_dispatcher = MessageDispatcher(self.component_entity_map)
        self.entity_factory = EntityFactory(self.component_entity_map)

    def mock(self):
        player_template = PlayerComponentSetTemplate()
        for _ in range(0, 2):
            self.entity_factory.create(player_template)

        mock_message = ( MessageTypes.GradesModification, {"value": 15, "target_entity_id": 1} )
        self.message_dispatcher.dispatch(*mock_message)
        self.message_dispatcher.dispatch(MessageTypes.ReportGrades)

    def performance_test(self):
        entity_count = 100000
        start = datetime.now()
        player_template = PlayerComponentSetTemplate()
        for _ in range(0, entity_count):
            self.entity_factory.create(player_template)

        mock_message = ( MessageTypes.GradesModification, {"value": 15, "target_entity_id": 1} )
        self.message_dispatcher.dispatch(*mock_message)
        end = datetime.now()
        elapsed = end - start
        print "Time to dispatch 1 message to {} entities:".format(str(entity_count)), elapsed.total_seconds()
        
    def load(self, game_id, user_id):
        pass