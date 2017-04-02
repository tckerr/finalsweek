class Student(object):

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.popularity = data["popularity"]
        self.grades = data["grades"]

class Seat(object):
  
    def __init__(self, data):
        self.id = data["id"]
        self.column = data["column"]
        self.row = data["row"]
        self.student = None
