from sim.entity.filtering.util.test_classes import (Student, Seat, ComponentType, CombinationLogic,)
from random import randint, shuffle
from copy import copy 

generic_filter = lambda component, requestor_component: True

filters = {
    Student: {
        "less_popularity" : lambda component, requestor_component: component.popularity < requestor_component.popularity,
        "id_not_me": lambda component, requestor_component: component.id != requestor_component.id,
        "less_grades" : lambda component, requestor_component: component.grades < requestor_component.grades,
    },
    Seat: {
        "col_same": lambda component, requestor_component: component.column == requestor_component.column,
        "row_lower": lambda component, requestor_component: component.row < requestor_component.row,
        "row_back": lambda component, requestor_component: component.row == 5,
    }
}

class TargetStrategyFieldsDefinition(object):
    fields = (
        "id",
        "combination_logic",
        "component_type",
        "returning_component_property",
        "count",
        "filters"
    )


class ObjectProvider(object):
    def get_by_type(self, cls):
        if cls is Student:
            return self.requestor_student
        if cls is Seat:
            return self.requestor_seat

class ContextProvider(object):
    size = 10
    seated_students = size - 3

    def __init__(self):
        self.students = [Student() for _ in range(0, self.size)]
        self.seats = []
        students_copy = copy(self.students)
        shuffle(students_copy)
        for idx in range(0, self.seated_students):
            self.seats.append(Seat(students_copy[idx]))
        for idx in range(0, self.size - self.seated_students):
            self.seats.append(Seat())            

        self.requestor_seat = self.seats[randint(1, self.seated_students-1)]
        self.requestor_student =  self.requestor_seat.student

    def requestor_by_type(self, cls):
        if cls is Student:
            return self.requestor_student
        if cls is Seat:
            return self.requestor_seat
    
    def all_of_type(self, cls):
        if cls is Student:
            return self.students
        if cls is Seat:
            return self.seats
    
    def resolve_filter_type(self, cls, component_filter_string):
        return filters[cls][component_filter_string]

class TargetStrategy(object): 

    @property
    def __is_leaf(self):
        return len(self.strategies) == 0

    @property
    def __is_root(self):
        return self.parent is None

    @property
    def __merge_results(self):
        return self.combination_logic == CombinationLogic.AND 

    def evaluate(self):
        '''Returns an array of component instance sets'''
        self.component_class = ComponentType.resolve_type(self.component_type)   

        requestor_component = self.context_provider.requestor_by_type(self.component_class)
        branch_results = self.__get_branch_results()                 
            
        if self.__merge_results or not self.__is_root:
            return self.__get_combined_result_set(branch_results, requestor_component)
        else:
            return self.__get_option_sets(branch_results, requestor_component)

    def __get_combined_result_set(self, result_set, requestor_component):
        if len(result_set) > 0 and result_set[0].__class__ is list:
            result_set = self.__merge(*result_set)
        deduped_result_set = self.__dedupe(result_set)
        filtered_result_set = self.__get_filtered_result_set(deduped_result_set, requestor_component)
        converted_result_set = self.__convert_result_set(filtered_result_set)
        return converted_result_set

    def __get_option_sets(self, result_set, requestor_component):
        unmerged_result_sets = []
        for unmerged_result_set in result_set:
            filtered_results = self.__get_filtered_result_set(unmerged_result_set, requestor_component)
            converted_results = self.__convert_result_set(unmerged_result_set) 
            unmerged_result_sets.append(converted_results)
        return unmerged_result_sets  

    def __get_branch_results(self):
        if self.__is_leaf:
            return self.__get_leaf_results()
        return self.__get_child_strategy_results()  

    def __get_leaf_results(self):
        assert self.__is_root or self.combination_logic == CombinationLogic.AND
        return self.context_provider.all_of_type(self.component_class)

    def __get_child_strategy_results(self):
        unmerged_child_results = []
        for child_strategy in self.strategies:
            child_strategy_result = child_strategy.evaluate()
            unmerged_child_results.append(child_strategy_result)           
        return unmerged_child_results        

    def __get_filtered_result_set(self,  component_list, requestor_component):
        for component_filter_string in self.filters:
            # TODO: builder
            component_filter = self.context_provider.resolve_filter_type(self.component_class, component_filter_string)
            component_list = self.__filter_list(component_filter, component_list, requestor_component)
        return component_list

    def __convert_result_set(self, result_set):
        if self.returning_component_property is None:
            return result_set    
        new_result_set = []
        for result in result_set:
            prop = getattr(result, self.returning_component_property)
            if prop:
                if self.parent:
                    assert prop.__class__ is self.parent.component_class
                new_result_set.append(prop)
        return new_result_set

    # util
    def __filter_list(self, component_filter, component_list, requestor_component):
        results = []
        for component in component_list:
            if component.__class__ is not requestor_component.__class__:
                print(component.__class__ , requestor_component.__class__)
                raise Exception()
            if component_filter(component, requestor_component):
                results.append(component)
        return results

    def __merge(self, *list_args):
        merged = []
        for item in list_args:
            merged += item
        return merged

    def __dedupe(self, component_list):
        return list(set(component_list))

