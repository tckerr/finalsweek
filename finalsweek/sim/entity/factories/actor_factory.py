from sim.entity.factories.entity_factory import EntityIdGenerator
from sim.exceptions import NotImplementedException
from sim.entity.components import (
    GradesComponent, 
    PopularityComponent,
    ActorComponent, )

class ActorFactory(object):
    def __init__(self, component_entity_map):
        self.component_entity_map = component_entity_map

    def create_user(self, user_id):
        return self.__build_components(user_id)     
    
    def create_ai(self):
        return self.__build_components()        

    def __build_components(self, user_id=None):
        entity_id = EntityIdGenerator.generate()
        self.__build_grades_component(entity_id)
        self.__build_popularity_component(entity_id)
        self.__build_actor_component(entity_id, user_id)
        return entity_id

    def __build_grades_component(self, entity_id):
        grades_component = GradesComponent()
        self.component_entity_map.insert(entity_id, grades_component)

    def __build_popularity_component(self, entity_id):
        popularity_component = PopularityComponent()
        self.component_entity_map.insert(entity_id, popularity_component)
             
    def __build_actor_component(self, entity_id, user_id):
        actor_component = ActorComponent()
        actor_component.user_id = user_id #otherwise AI
        self.component_entity_map.insert(entity_id, actor_component)