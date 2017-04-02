from sim.entity.filtering.util.test_classes import (Student, Seat,)

class ContextProvider(object):

    def __init__(self, dictionary):
        self.students = []
        self.seats = []
        self.requestor_student = None
        self.requestor_seat = None

        for student_data in dictionary["students"]:
            student = Student(student_data)
            if student.id == dictionary["requestor_student_id"]:
                self.requestor_student = student
            self.students.append(student)

        for seat_data in dictionary["seats"]:
            self.seats.append(Seat(seat_data))

        for seat_mapping in dictionary["seat_map"]:
            student = self.__get(self.students, id=seat_mapping["student_id"])
            seat = self.__get(self.seats, row=seat_mapping["row"], column=seat_mapping["column"])
            seat.student = student

        self.requestor_seat = self.__get(self.seats, student=self.requestor_student)

    def __get(self, arr, **values):
        for item in arr:
            failed = False
            for key, value in values.items():
                if not getattr(item, key) == value:
                    failed = True
            if not failed:
                return item    

    def requestor_by_type(self, cls):
        if cls is Student:
            return self.requestor_student
        if cls is Seat:
            return self.requestor_seat
    
    def all_of_type(self, cls):
        if cls is Student:
            return self.students
        if cls is Seat:
            return self.seats