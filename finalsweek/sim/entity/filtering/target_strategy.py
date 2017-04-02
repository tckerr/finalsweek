from sim.entity.filtering.util.helpers import (merge, flatten, filter_list) 

class TargetStrategy(object): 

    @property
    def __is_leaf(self):
        return len(self.strategies) == 0

    @property
    def __is_root(self):
        return self.parent is None

    @property
    def __flatten_results(self):
        return self.combination_logic == "and" #or not self.__is_root

    def evaluate(self):
        '''Returns an array of component instance sets'''        
        branch_results = self.__get_branch_results() 
        if self.__flatten_results:
            flattened_results = flatten(branch_results)
            return self.__filter_and_convert(flattened_results)
        else:
            return list(map(self.__filter_and_convert, branch_results))

    def __get_branch_results(self):
        if self.__is_leaf:
            return self.__get_leaf_results()
        return self.__evaluate_child_strategies() 

    def __get_leaf_results(self):
        assert self.__is_root or self.__flatten_results
        return getattr(self.context_provider.context, self.components_source)

    def __evaluate_child_strategies(self):
        return [strategy.evaluate() for strategy in self.strategies]

    def __filter_and_convert(self, result_set):
        filtered = self.__filter(result_set)
        if self.returning_component_property is not None:
            return self.__convert(filtered)
        return filtered

    def __filter(self, component_list):
        for filter_fn in self.filters:
            component_list = filter_list(filter_fn, component_list)
        return component_list

    def __convert(self, result_set): 
        new_result_set = []
        for result in result_set:
            prop = getattr(result, self.returning_component_property)
            if prop:
                new_result_set.append(prop)
        return new_result_set