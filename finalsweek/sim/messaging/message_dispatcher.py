from sim.messaging.message_types import MessageTypes
from sim.entity.providers import ComponentEntityMap

class MessageDispatcher(object):
    def __init__(self, game_id):
        self.component_entity_map = ComponentEntityMap(game_id)
        self.message_types = set()
        self.__init_message_types()

    def __init_message_types(self):
        default_message_types = MessageTypes.all_types()
        self.message_types.update(default_message_types)

    def dispatch(self, message_type, data=None):
        assert message_type in self.message_types
        if data is None:
            data = {}
        if "target_entity_id" in data:
            self.__dispatch_to_entity(message_type, data, data["target_entity_id"])
        else:
            self.__dispatch_to_all(message_type, data)

    def __dispatch_to_all(self, message_type, data):
        components = self.component_entity_map.list_components()
        self.__send_message_to_component_list(components, message_type, data)

    def __dispatch_to_entity(self, message_type, data, entity_id):
        components = self.component_entity_map.list_components_by_entity_id(entity_id)
        self.__send_message_to_component_list(components, message_type, data)

    def __send_message_to_component_list(self, component_list, message_type, data):
        for component in component_list:
            component.msg(message_type, data)