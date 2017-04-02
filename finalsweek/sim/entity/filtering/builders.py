from sim.entity.filtering.target_strategy import TargetStrategy
from sim.entity.filtering.providers import FilterProvider

class TargetStrategyBuilder(object):   

    def build(self, dictionary, context_provider, type_provider, filter_provider=None, parent_strategy=None):
        strategy = TargetStrategy()
        filter_provider = filter_provider or FilterProvider()
        self.__init_fields(dictionary, context_provider, type_provider, filter_provider, strategy)
        strategy.context_provider = context_provider
        strategy.parent = parent_strategy
        return strategy

    def __init_fields(self, dictionary, context_provider, type_provider, filter_provider, strategy):
        self.__init_source(dictionary, strategy)
        self.__init_id( dictionary, strategy)
        self.__init_combination_logic(dictionary, strategy)
        self.__init_components_source(dictionary, strategy)
        self.__init_returning_component_property( dictionary, strategy)
        self.__init_count(dictionary, strategy)
        self.__init_filters(dictionary, strategy, filter_provider, context_provider)
        self.__init_strategies(dictionary, strategy, context_provider, type_provider, filter_provider)

    def __init_source(self, dictionary, strategy):
        strategy.source = dictionary

    def __init_id(self, dictionary, strategy):
        strategy.id = dictionary["id"]

    def __init_combination_logic(self, dictionary, strategy):
        strategy.combination_logic = dictionary["combination_logic"]

    def __init_components_source(self, dictionary, strategy):
        strategy.components_source = dictionary.get("components_source", None)

    def __init_returning_component_property(self, dictionary, strategy):
        strategy.returning_component_property = dictionary["returning_component_property"]

    def __init_count(self, dictionary, strategy):
        strategy.count = dictionary["count"]
        
    def __init_filters(self, dictionary, strategy, filter_provider, context_provider):  
        filters = [filter_provider.resolve(obj_filter, context_provider) for obj_filter in dictionary["filters"]]
        strategy.filters = filters

    def __init_strategies(self, dictionary, strategy, context_provider, type_provider, filter_provider):
        strategies = [self.build(strategy_data, context_provider, type_provider, filter_provider=filter_provider, parent_strategy=strategy) for strategy_data in dictionary["strategies"]]
        strategy.strategies = strategies
