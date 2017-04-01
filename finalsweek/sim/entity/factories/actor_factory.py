from sim.exceptions import NotImplementedException
from sim.entity.entity import Entity
from sim.entity.components import (
    GradesComponent, 
    PopularityComponent,
    ActorComponent, )

class ActorFactory(object):
    def create_user(self, game_id, user_id):
        component = self.__build_components(game_id, user_id)     
    
    def create_ai(self, game_id):
        return self.__build_components(game_id)     

    def __build_entity(self, game_id):
        entity = Entity()
        entity.game_id = game_id
        entity.save()
        return entity

    def __build_components(self, game_id, user_id=None):
        entity_id = self.__build_entity(game_id).id
        self.__build_grades_component(entity_id)
        self.__build_popularity_component(entity_id)
        self.__build_actor_component(entity_id, user_id)
        return entity_id    

    def __build_grades_component(self, entity_id):
        grades_component = GradesComponent()
        grades_component.entity_id = entity_id
        grades_component.save()

    def __build_popularity_component(self, entity_id):
        popularity_component = PopularityComponent(entity_id)
        popularity_component.entity_id = entity_id
        popularity_component.save()
             
    def __build_actor_component(self, entity_id, user_id):
        actor_component = ActorComponent(entity_id)
        actor_component.entity_id = entity_id
        actor_component.user_id = user_id #otherwise AI
        actor_component.save()
