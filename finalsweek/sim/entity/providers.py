from sim.messaging.message_types import MessageTypes
from sim.entity.components import *

class ComponentEntityMap(object):

    mapped_component_types = (
        PopularityComponent,
        TurnComponent,
        GradesComponent,
        CostComponent,
        DisposableComponent,
        ActionComponent,
        StackableComponent,
        VisibilityComponent,
        ActorComponent, )

    def __init__(self, game_id):
        self.__game_id = game_id

    def list_components(self, **filters):
        for component_type in self.mapped_component_types:
            for component in self.list_components_by_component_type(component_type, **filters):
                yield component

    def list_components_by_component_type(self, component_type, **filters):
        for component in component_type.objects.filter(entity__game_id=self.__game_id, **filters):
            yield component

    def list_components_by_entity_id(self, entity_id):
        for component in self.list_components(entity_id=entity_id):
            yield component
    
    def delete_component(self, component):
        component.delete()

    def move_component(self, component, entity_id):
        component.entity_id = entity_id
        component.save()

class ComponentProvider(object):
    component_type = None

    def __init__(self, game_id):
        self.component_entity_map = ComponentEntityMap(game_id)

    @property
    def all(self):
        return self.component_entity_map.list_components_by_component_type(self.__class__.component_type)

class ActorProvider(ComponentProvider):
    component_type = ActorComponent 