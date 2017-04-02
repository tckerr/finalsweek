from sim.entity.filtering.target_strategy import TargetStrategyFieldsDefinition

class TargetStrategyPrinter(object):
    padding_per_level = 5

    def print(self, root_strategy):
        print(self.get_str(root_strategy))

    def get_str(self, root_strategy):
        return self.__print_repr(root_strategy, 0)

    def __print_repr(self, strategy, padding):
        text = ""
        pad_str = "".join([" " for _ in range(0, padding)])
        text += pad_str + "[{}]".format(strategy.__class__.__name__) + "\n"

        for field in TargetStrategyFieldsDefinition.fields:  
            text += self.__print_field_with_padding(strategy, pad_str, field) + "\n"

        for strategy in strategy.strategies:
            new_padding = padding + self.padding_per_level
            text += self.__print_repr(strategy, new_padding)

        return text

    def __print_field_with_padding(self, strategy, pad_str, field_name):
        text = "{}{}: {}".format(pad_str, field_name, str(getattr(strategy, field_name)))        
        return text