from sim.entity.filtering.target_strategy import TargetStrategy
from sim.entity.filtering.providers import FilterProvider, TypeProvider

class TargetStrategyBuilder(object):   

    def __init__(self):
        self.filter_provider = FilterProvider()
        self.type_provider = TypeProvider()

    def build(self, dictionary, context_provider, parent_strategy=None):
        strategy = TargetStrategy()
        self.__init_fields(dictionary, strategy, context_provider)
        strategy.context_provider = context_provider
        strategy.parent = parent_strategy
        return strategy

    def __init_fields(self, dictionary, strategy, context_provider):
        self.__init_source(dictionary, strategy)
        self.__init_id( dictionary, strategy)
        self.__init_combination_logic(dictionary, strategy)
        self.__init_component_type(dictionary, strategy)
        self.__init_returning_component_property( dictionary, strategy)
        self.__init_count(dictionary, strategy)
        self.__init_filters(dictionary, strategy)
        self.__init_strategies(dictionary, strategy, context_provider)

    def __init_source(self, dictionary, strategy):
        strategy.source = dictionary

    def __init_id(self, dictionary, strategy):
        strategy.id = dictionary["id"]

    def __init_combination_logic(self, dictionary, strategy):
        strategy.combination_logic = dictionary["combination_logic"]

    def __init_component_type(self, dictionary, strategy):
        component_type = self.type_provider.resolve(dictionary["component_type"]) 
        strategy.component_type = component_type

    def __init_returning_component_property(self, dictionary, strategy):
        strategy.returning_component_property = dictionary["returning_component_property"]

    def __init_count(self, dictionary, strategy):
        strategy.count = dictionary["count"]
        
    def __init_filters(self, dictionary, strategy):        
        filters = [self.filter_provider.resolve(strategy.component_type, filter_str) for filter_str in dictionary["filters"]]
        strategy.filters = filters

    def __init_strategies(self, dictionary, strategy, context_provider):
        strategies = [self.build(strategy_data, context_provider, strategy) for strategy_data in dictionary["strategies"]]
        strategy.strategies = strategies
