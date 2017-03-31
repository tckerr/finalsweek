# todo: map components seperately

class MessageTypes(object):
    GradesModification = "GradesModification"
    ReportGrades = "ReportGrades"
  
class MessageDispatcher(object):
    def __init__(self, entity_provider):
        self.__entity_provider = entity_provider
        self.message_types = set()
        self.__init_message_types()

    def __init_message_types(self):
        default_message_types = (
            value for key, value in MessageTypes.__dict__.items() if not key.startswith("__")
        )
        self.message_types.update(default_message_types)

    def dispatch(self, message_type, data=None):
        assert message_type in self.message_types
        if data is None:
            data = {}
        if "target_entity_id" in data:
            self.__dispatch_to_entity(data["target_entity_id"], message_type, data)
        else:
            self.__dispatch_to_all(message_type, data)

    def __dispatch_to_all(self, message_type, data):
        for entity in self.__entity_provider.entities:
            entity.receive_message(message_type, data)

    def __dispatch_to_entity(self, id, message_type, data):
        entity = self.__entity_provider.with_id(id)
        if entity:
            entity.receive_message(message_type, data)

# ----------------------------

class Component(object): pass

class IntegerComponent(Component):

    def __init__(self, *args, **kwargs):
        self.__value = 0
        super(IntegerComponent, self).__init__(*args, **kwargs)

    def add(self, value):
        self.__value += value

    def remove(self, value):
        self.add(-1 * value)

    @property
    def value(self):
        return self.__value

    def receive_message(self, message_type, data):
        pass
        # overwrite me!!

class GradesComponent(IntegerComponent):
    def receive_message(self, message_type, data):
        if message_type is MessageTypes.GradesModification:
            self.add(data["value"])

        if message_type is MessageTypes.ReportGrades:
            print self.value

class PopularityComponent(IntegerComponent): pass
class TurnComponent(Component): pass

# ----------------------------

class Entity(object):
    incr = 0    

    def __init__(self, components=[]):
        self.id = Entity.incr;
        Entity.incr += 1
        self.components = {}
        for component in components:
            self.add_component(component)

    def add_component(self, component):
        assert issubclass(component.__class__, Component)
        self.components[component.__class__] = component

    def get_component(self, component_type):
        if component_type in self._components:
            return self.components[component.__class__]

    def receive_message(self, message_type, data):
        for component_class, component in self.components.iteritems():
            component.receive_message(message_type, data)


class ComponentEntityMap(object):
    pass

# change to ComponentEntityMap
class EntityProvider(object):

    def __init__(self, entities=[]):
        self.__entities = set()
        for entity in entities:
            self.add_entity(entity)

    def add_entity(self, entity):
        assert issubclass(entity.__class__, Entity)
        self.__entities.add(entity)

    @property
    def entities(self):
        return self.__entities

    def with_id(self, id):
        for entity in self.__entities:
            if entity.id == id:
                return entity

    def with_component(self, component_type):
        return self.with_components((component_type,))

    def with_components(self, component_type_list):
        for entity in self.__entities:
            if all(component_type in entity.components for component_type in component_type_list):
                yield entity

class PlayerEntityFactory(object):

    def create(self,):
        components = self.build_default_components()
        return Entity(components)

    def build_default_components(self):
        return [
            GradesComponent(),
            PopularityComponent(),
            PopularityComponent() ]


# ----------------------------

class TurnManager(object):
    def __init__(self):
        self.components = []
        self.current_turn = 0

    def add_turn_component(self, component):
        assert issubclass(component.__class__, TurnComponent)
        self.components.append(component)

    def get_current_turn(self, component):
        return self.components[self.current_turn]

    def advance(self):
        # who is in charge of managing this?
        pass


# -----------------------

class GameInitializer(object):

    def __init__(self):
        self.entity_provider = EntityProvider()
        self.message_dispatcher = MessageDispatcher(self.entity_provider)
        self.player_entity_factory = PlayerEntityFactory()

    def new(self):
        player_one = self.player_entity_factory.create()
        player_two = self.player_entity_factory.create()
        self.entity_provider.add_entity(player_one)
        self.entity_provider.add_entity(player_two)


        mock_message = ( MessageTypes.GradesModification, {"value": 15, "target_entity_id": 0} )
        self.message_dispatcher.dispatch(*mock_message)
        self.message_dispatcher.dispatch(MessageTypes.ReportGrades)
        
    def load(self, game_id, user_id):
        pass



GameInitializer().new()