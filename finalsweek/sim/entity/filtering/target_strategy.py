class ComponentType(object):
    SEAT = "seat"
    OR = "student"

class CombinationLogic(object):
    AND = "and"
    OR = "or"

class TargetStrategyFieldsDefinition(object):
    fields = (
        "id",
        "combination_logic",
        "component_type",
        "returning_component_property",
        "count",
        "filters"
    )


class TargetStrategy(object): 

    pass



