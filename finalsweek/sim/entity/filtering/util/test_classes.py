from random import randint

class Student(object):
    safe_int = 999

    def __init__(self):
        Student.safe_int += 1
        self.id = Student.safe_int
        self.grades = randint(1, 100)
        self.popularity = randint(1, 100)

class Seat(object):
    safe_int = 9999
  
    def __init__(self, student=None):
        Seat.safe_int += 1
        self.id = Seat.safe_int
        self.student = student
        self.row = randint(1, 5)
        self.column = randint(1, 5)

class ComponentType(object):

    @classmethod
    def resolve_type(cls, val):
        if val == cls.SEAT:
            return Seat
        if val == cls.STUDENT:
            return Student

    SEAT = "seat"
    STUDENT = "student"

class CombinationLogic(object):
    AND = "and"
    OR = "or"
