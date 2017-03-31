from sim.messaging.message_types import MessageTypes
from sim.entity.components import Component


class EntityFactory(object):
    __entity_incr = 0
    __component_incr = 0

    def __generate_entity_id(self):
        self.__entity_incr += 1
        return self.__entity_incr

    def __generate_component_id(self):
        self.__component_incr += 1
        return self.__component_incr

    def __init__(self, component_entity_map):
        self.component_entity_map = component_entity_map

    def create(self, template):
        entity_id = self.__generate_entity_id()
        for component in template.build(self.__generate_component_id):
            self.component_entity_map.insert(entity_id, component)
        return entity_id


class ComponentEntityMap(object):
    top_level_components = MessageTypes.all_types()

    def __init__(self):
        self.__component_types = { component_type: set() for component_type in self.top_level_components }
        self.__entities = {}
        self.__components = {}

    def insert(self, entity_id, component):
        component_type = component.__class__
        assert issubclass(component_type, Component)
        self.__safe_add(self.__component_types, component_type, component)
        self.__safe_add(self.__entities, entity_id, component)
        self.__assign(self.__components, component.id, component)

    def list_components(self):
        for component_id, component in self.__components.iteritems():
            yield component

    def list_components_by_component_type(self, component_type):
        for component in self.__safe_list(self.__component_types, component_type):
            yield component

    def list_components_by_entity_id(self, entity_id):
        for component in self.__safe_list(self.__entities, entity_id):
            yield component

    def get_component_by_id(self, component_id):
        return self.__safe_get(self.__components, component_id)

    def get_entity_id_by_component(self, input_component):
        for entity_id, component_set in self.__entities.iteritems():
            for component in component_set:
                if component is input_component:
                    return entity_id
    
    def delete_component(self, component):
        entity_id = self.get_entity_id_by_component(component)
        self.__safe_delete(self.__entities, entity_id, component)
        self.__safe_delete(self.__component_types, component.__class__, component)
        del self.__components[component.id]

    def move_component(self, component, entity_id):
        self.delete_component(component)
        self.insert(entity_id, component)

    def __safe_add(self, dictionary, index, value):
        if index not in dictionary:
            dictionary[index] = set()
        dictionary[index].add(value)

    def __assign(self, dictionary, index, value):
        dictionary[index] = value

    def __safe_list(self, dictionary, index):
        if index not in dictionary:
            return set()
        return dictionary[index]

    def __safe_get(self, dictionary, index):
        if index in dictionary:
            return dictionary[index]

    def __safe_delete(self, dictionary, index, value):
        if index in dictionary:
            dictionary[index].discard(value)