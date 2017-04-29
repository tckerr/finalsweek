import uuid


class I:
    integer = -1


def integer_id():
    I.integer += 1
    return I.integer


def guid():
    return str(uuid.uuid4())


def floor_at_zero(val):
    return max(0, val)


def set_in_dict(dct, k, v):
    dct[k] = v
