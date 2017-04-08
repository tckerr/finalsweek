from sim.entity.components import *

class ComponentSetTemplate(object):
    components = ()

    def build(self, component_id):
        return (component_type(component_id) for component_type in self.components)

class ActorComponentSetTemplate(ComponentSetTemplate):
    components = [
        GradesComponent,
        PopularityComponent,
        TurnComponent,
        ActorComponent
    ]


'''
what I can play = ActionComponent w/ no CostComponent or CostComponent I can afford
'''