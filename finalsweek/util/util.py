import string

from game.configuration.settings import generation


class I:
    integer = -1


def integer_id():
    I.integer += 1
    return I.integer


def guid():
    #return str(uuid.uuid4())
    return random_id()


def random_id():
    length = range(0, generation["id_len"])
    return "".join([generation["random"].choice(string.ascii_letters) for _ in length])


def floor_at_zero(val):
    return max(0, val)


def set_in_dict(dct, k, v):
    dct[k] = v


