class TargetStrategyPrinter(object):
    padding_per_level = 6
    assert padding_per_level % 2 is 0
    fields = (
        "id",
        "combination_logic",
        "returning_component_property",
        "count"
    )

    def print(self, root_strategy):
        print(self.get_str(root_strategy))

    def get_str(self, root_strategy):
        return self.__print_repr(root_strategy, 0)

    def __print_repr(self, strategy, padding):
        text = ""
        pad_str = self.__get_indent(padding)
        text += pad_str + "[{}]".format(strategy.__class__.__name__) + "\n"

        for field in self.fields:  
            text += self.__print_field_with_padding(strategy, pad_str, field) + "\n"

        text += "{}{}: {}\n".format(pad_str, "component_source", strategy.source.get("component_source", "None"))


        filters_str = ",  Dynamic: [" + str([ f for f in strategy.source["filters"]]) + "]"
        text += "{}{}: {}\n".format(pad_str, "filters", filters_str)

        for strategy in strategy.strategies:
            new_padding = padding + self.padding_per_level
            text += self.__print_repr(strategy, new_padding)

        return text

    def __print_field_with_padding(self, strategy, pad_str, field_name):
        text = "{}{}: {}".format(pad_str, field_name, str(getattr(strategy, field_name)))        
        return text

    def __get_indent(self, padding):
        return "".join([" " for _ in range(0, padding)])