import random as __random
import string

import names as __names

from game.configuration.settings import generation

__seeded_random = __random.Random(generation["seed"])
__random.random = __seeded_random.random


def random_id():
    length = range(0, generation["id_len"])
    return "".join([__seeded_random.choice(string.ascii_letters) for _ in length])


def random_name():
    return __names.get_full_name(gender="female")


def shuffle(lst):
    return __seeded_random.shuffle(lst)


def choice(lst):
    return __seeded_random.choice(lst)
