from sim.entity.filtering.target_strategy import TargetStrategyFieldsDefinition, TargetStrategy

class TargetStrategyBuilder(object):   

    def build(self, dictionary, context_provider, parent_strategy=None):
        strategy = TargetStrategy()
        self.__init_fields(dictionary, strategy, context_provider)
        strategy.context_provider = context_provider
        strategy.parent = parent_strategy
        return strategy

    def __init_fields(self, dictionary, strategy, context_provider):
        for field in TargetStrategyFieldsDefinition.fields:
            self.__init_field(field, dictionary, strategy)
        strategies = [self.build(strategy_data, context_provider, strategy) for strategy_data in dictionary["strategies"]]
        setattr(strategy, "strategies", strategies)

    def __init_field(self, field_name, dictionary, strategy):
        value = dictionary[field_name]
        setattr(strategy, field_name, value)