class EntityIdGenerator(object):
    __entity_incr = 0

    @classmethod
    def generate(cls):
        cls.__entity_incr += 1
        return cls.__entity_incr



class EntityFactory(object):
    __entity_incr = 0
    __component_incr = 0

    def __init__(self, component_entity_map):
        self.component_entity_map = component_entity_map
   
    def create(self, template):
        entity_id = EntityIdGenerator.generate()
        components = [component for component in template.build()]
        for components in components:
            self.component_entity_map.insert(entity_id, component)
        return entity_id, components
