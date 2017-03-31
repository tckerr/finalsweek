from django.core.management.base import BaseCommand
#
from sim.messages.message_types import MessageTypes
from sim.messages.message_dispatcher import MessageDispatcher
from sim.components.components import (
    Component, 
    GradesComponent, 
    PopularityComponent, 
    TurnComponent,
)


class ComponentEntityMap(object):
    top_level_components = MessageTypes.all_types()

    def __init__(self):
        self.__components = { component_type: set() for component_type in self.top_level_components }
        self.__entities = {}

    def insert(self, entity_id, component):
        component_type = component.__class__
        assert issubclass(component_type, Component)
        self.__safe_add(self.__components, component_type, component)
        self.__safe_add(self.__entities, entity_id, component)

    def get_all(self):
        for component_type, component_list in self.__components.iteritems():
            for component in component_list:
                yield component

    def get_by_component_type(self, component_type):
        for component in self.__safe_retrieve(self.__components, component_type):
            yield component

    def get_by_entity_id(self, entity_id):
        for component in self.__safe_retrieve(self.__entities, entity_id):
            yield component

    def remove_by_entity_id(self, entity_id, component):
        self.__safe_delete(self.__entities, entity_id, component)

    def __safe_add(self, dictionary, index, value):
        if index not in dictionary:
            dictionary[index] = set()
        dictionary[index].add(value)

    def __safe_retrieve(self, dictionary, index):
        if index not in dictionary:
            return set()
        return dictionary[index]

    def __safe_delete(self, dictionary, index, value):
        if index in dictionary:
            dictionary[index].discard(value)


class ComponentSetTemplate(object):
    components = ()

    def build(self):
        return (component_type() for component_type in self.components)

class PlayerComponentSetTemplate(ComponentSetTemplate):
    components = (
        GradesComponent,
        PopularityComponent,
        TurnComponent
    )

class EntityFactory(object):
    __incr = 0

    def __generate_id(self):
        self.__incr += 1
        return self.__incr

    def __init__(self, component_entity_map):
        self.component_entity_map = component_entity_map

    def create(self, template):
        entity_id = self.__generate_id()
        for component in template.build():
            self.component_entity_map.insert(entity_id, component)
        return entity_id


# -----------------------

class GameInitializer(object):

    def __init__(self):
        self.component_entity_map = ComponentEntityMap()
        self.message_dispatcher = MessageDispatcher(self.component_entity_map)
        self.entity_factory = EntityFactory(self.component_entity_map)

    def new(self):
        player_template = PlayerComponentSetTemplate()
        self.entity_factory.create(player_template)
        self.entity_factory.create(player_template)

        mock_message = ( MessageTypes.GradesModification, {"value": 15, "target_entity_id": 1} )
        self.message_dispatcher.dispatch(*mock_message)
        self.message_dispatcher.dispatch(MessageTypes.ReportGrades)
        
    def load(self, game_id, user_id):
        pass




class Command(BaseCommand):
    def handle(self, *args, **options):
        # now do the things that you want with your models here
        
        GameInitializer().new()
