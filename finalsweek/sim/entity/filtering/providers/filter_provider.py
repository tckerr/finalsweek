filters = {
    "Student": {
        "less_popularity" : lambda component, requestor_component: component.popularity < requestor_component.popularity,
        "lte_popularity" : lambda component, requestor_component: component.popularity <= requestor_component.popularity,
        "id_not_me": lambda component, requestor_component: component.id != requestor_component.id,
        "id_me": lambda component, requestor_component: component.id == requestor_component.id,
        "less_grades" : lambda component, requestor_component: component.grades < requestor_component.grades,
    },
    "Seat": {
        "col_same": lambda component, requestor_component: component.column == requestor_component.column,
        "row_same": lambda component, requestor_component: component.row == requestor_component.row,
        "row_lower": lambda component, requestor_component: component.row < requestor_component.row,
        "row_back": lambda component, requestor_component: component.row == 4,
    }
}

class FilterProvider(object):
    operator_functions = {
        "<=":   lambda x, y: x <= y,
        "<":    lambda x, y: x <  y,
        ">=":   lambda x, y: x >= y,
        ">":    lambda x, y: x >  y,
        "==":   lambda x, y: x == y
    }

    def __init__(self):
        self.__function_cache = {}

    def resolve(self, type, data):
        if data.__class__ is str:
            return filters[type.__name__][data]
        else:
            print("DYNAMIC")
            return self.__resolve_dynamic(data)

    def __resolve_dynamic(self, data):    
        operator = data["operator"]
        operand_property_name = data["property"]
        comparison_value = data["comparison_value"] # could be a prop
        filter_type = data["filter_type"]
        cache_args = map(str, [operand_property_name, operator, comparison_value, filter_type,])

        cache_result = self.__get_from_cache(*cache_args)
        if cache_result:
            return cache_result

        operator_function = self.__resolve_operator(operator)
        if filter_type == "context_comparitor":
            fn = self.__generate_comparitor(operator_function, operand_property_name, comparison_value)
        elif filter_type == "evaluation":
            fn = self.__generate_evaluation(operator_function, operand_property_name, comparison_value)

        self.__cache_fn(fn, *cache_args)
        return fn

    def __resolve_operator(self, value):
        return self.operator_functions[value]

    def __cache_fn(self, fn, *cache_args):
        cache_key = self.__build_cache_key(*cache_args)
        print(cache_key)
        self.__function_cache[cache_key] = fn

    def __get_from_cache(self, *args):
        cache_key = self.__build_cache_key(*args)
        return self.__function_cache[cache_key] if cache_key in self.__function_cache else None

    def __build_cache_key(self, *args):
        return "#".join([key if key else "$$none" for key in args ])

    def __generate_comparitor(self, operator_function, operand_property_name, comparison_property_name):
        def fn(operand, comparison_value):
            operand_property = getattr(operand, operand_property_name) if operand_property_name else operand
            comparison_property = getattr(operand, comparison_property_name) if comparison_property_name else comparison_value
            return operator_function(operand_property, comparison_property)
        return fn 

    def __generate_evaluation(self, operator_function, operand_property_name, comparison_value):
        def fn(operand, _=None):
            operand_property = getattr(operand, operand_property_name) if operand_property_name else operand
            return operator_function(operand_property, comparison_value)
        return fn