def merge(list_list):
    merged = [item for sublist in list_list for item in sublist]
    return list(set(merged))

def flatten(nested_list):
    while len(nested_list) > 0 and nested_list[0].__class__ is list:
        nested_list = merge(nested_list)
    return nested_list

def filter_list(filter_function, item_list, comparitive_property):
    results = filter(lambda x: filter_function(x, comparitive_property), item_list)
    return list(results)
