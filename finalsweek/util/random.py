import string
import sys

import names as __names

from game.configuration.settings import generation

this = sys.modules[__name__]


def reseed(seed=None):
    import random as __new_random
    this.__seeded_random = __new_random.Random(seed or generation["seed"])


reseed()


def random_id():
    length = range(0, generation["id_len"])
    return "".join([this.__seeded_random.choice(string.ascii_letters) for _ in length])


def random_name():
    return __names.get_full_name(gender="female")


def shuffle(lst):
    return this.__seeded_random.shuffle(lst)


def choice(lst):
    return this.__seeded_random.choice(lst)
