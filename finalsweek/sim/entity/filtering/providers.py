from abc import abstractmethod, ABCMeta
from sim.entity.filtering.util.helpers import getprop, DictWrapper

class ContextProvider(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.context = DictWrapper()

    @abstractmethod
    def resolve_operator(self, operator_str):
        raise Exception( ("Filter received an non-standard operator \"{}\", " +\
                         "yet resolve_operator has not been defined. " +\
                         "Please override resolve_operator in your context "+\
                         "provider.").format(operator_str))

    @property
    def __not_implemented(self):
        return Exception("Method requires implementation")

class FilterProvider(object):
    operator_functions = {
        "<=":   lambda x, y: x <= y,
        "<":    lambda x, y: x <  y,
        ">=":   lambda x, y: x >= y,
        ">":    lambda x, y: x >  y,
        "==":   lambda x, y: x == y,
        "!=":   lambda x, y: x != y
    }

    def __init__(self):
        # TODO: alaises
        self.__function_cache = {}

    def resolve(self, data, context_provider):    
        operator = data["operator"]
        operand_property_name = data["property"]
        comparison_value = data["comparison_value"] # could be a prop
        filter_type = data["filter_type"]
        cache_args = map(str, [operand_property_name, operator, comparison_value, filter_type,])

        cache_result = self.__get_from_cache(*cache_args)
        if cache_result:
            return cache_result

        operator_function = self.__resolve_operator(operator, context_provider)
        if filter_type == "context":
            fn = self.__generate_context_comparitor(operator_function, operand_property_name, comparison_value, context_provider)
        elif filter_type == "evaluation":
            fn = self.__generate_evaluation(operator_function, operand_property_name, comparison_value)

        self.__cache_fn(fn, *cache_args)
        return fn

    def __resolve_operator(self, value, context_provider):
        default = self.operator_functions.get(value, False)
        return default if default else context_provider.resolve_operator(value)

    def __cache_fn(self, fn, *cache_args):
        cache_key = self.__build_cache_key(*cache_args)
        self.__function_cache[cache_key] = fn

    def __get_from_cache(self, *args):
        cache_key = self.__build_cache_key(*args)
        return self.__function_cache[cache_key] if cache_key in self.__function_cache else None

    def __build_cache_key(self, *args):
        return "#".join([key if key else "$.none" for key in args ])

    def __generate_context_comparitor(self, operator_function, operand_property_name, comparison_property_name, context_provider):
        def fn(operand):
            comparison_value = getprop(context_provider.context, comparison_property_name)
            if comparison_value is None or comparison_value.__class__ == DictWrapper:
                raise Exception("Value is None or not defined in context: {}".format(comparison_property_name) )
            operand_property = getattr(operand, operand_property_name) if operand_property_name else operand
            return operator_function(operand_property, comparison_value)
        return fn 

    def __generate_evaluation(self, operator_function, operand_property_name, comparison_value):
        def fn(operand):
            operand_property = getattr(operand, operand_property_name) if operand_property_name else operand
            return operator_function(operand_property, comparison_value)
        return fn

