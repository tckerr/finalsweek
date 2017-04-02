from sim.entity.filtering.util.test_classes import (Student, Seat,)

class TypeProvider(object):

    def resolve(self, val):
        if val == "seat":
            return Seat
        if val == "student":
            return Student