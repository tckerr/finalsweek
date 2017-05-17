def floor_at_zero(val):
    return max(0, val)


def set_in_dict(dct, k, v):
    dct[k] = v


def write_to_disk(file_name, string):
    with open(file_name, "a+") as file:
        file.write(string)
