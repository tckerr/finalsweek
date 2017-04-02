from sim.entity.filtering.target_strategy import TargetStrategyFieldsDefinition, TargetStrategy

class TargetStrategyBuilder(object):   

    def build(self, dictionary):
        strategy = TargetStrategy()
        self.__init_fields(dictionary, strategy)
        return strategy

    def __init_fields(self, dictionary, strategy):
        for field in TargetStrategyFieldsDefinition.fields:
            self.__init_field(field, dictionary, strategy)
        strategies = [self.build(strategy_data) for strategy_data in dictionary["strategies"]]
        setattr(strategy, "strategies", strategies)

    def __init_field(self, field_name, dictionary, strategy):
        value = dictionary[field_name]
        setattr(strategy, field_name, value)