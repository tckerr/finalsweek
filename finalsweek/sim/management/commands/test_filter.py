from django.core.management.base import BaseCommand
from sim.entity.filtering.builders import TargetStrategyBuilder
from sim.entity.filtering.providers import ContextProvider
from sim.entity.filtering.util.printers import TargetStrategyPrinter
import json, os

class JsonLoader(object):

    def load(self, path):
        with open(path, 'r', encoding='utf-8') as jsonfile:
            return json.loads(jsonfile.read())

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

class TypeProvider(object):

    def resolve(self, val):
        if val == "seat":
            return Seat
        if val == "student":
            return Student



class FinalsWeekContextProvider(ContextProvider):

    def __init__(self, dictionary, *args, **kwargs):
        super(FinalsWeekContextProvider, self).__init__(*args, **kwargs)
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

        self.__init_context()

    def __init_context(self):
        self.context.students = self.students
        self.context.seats = self.seats
        self.context.requestor.student = self.requestor_student
        self.context.requestor.seat = self.requestor_seat


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


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.json_loader = JsonLoader()
        self.builder = TargetStrategyBuilder()
        self.printer = TargetStrategyPrinter()

    def handle(self, *args, **options):
        strategy_json_path = os.path.dirname(__file__) + '/fixtures/filters_advanced.json'        
        seed_json_path = os.path.dirname(__file__) + '/fixtures/student_seed.json'        
        strategy_data = self.json_loader.load(strategy_json_path)      
        seed_data = self.json_loader.load(seed_json_path)      

        context_provider = FinalsWeekContextProvider(seed_data)
        type_provider = TypeProvider()
        root_strategy = self.builder.build(strategy_data, context_provider, type_provider)
        self.printer.print(root_strategy)

        results = root_strategy.evaluate()
        self.__print_results(results, context_provider)

    def __print_results(self, results, context_provider):
        print ("--- results ---")
        requestor_seat = context_provider.requestor_by_type(Seat)
        requestor_student = context_provider.requestor_by_type(Student)
        print("Requestor Seat -- ID: {}, Row: {}, Col: {}".format(str(requestor_seat.id),str(requestor_seat.row),str(requestor_seat.column)))
        print("Requestor Student ID: {}, Grades: {}, Pop: {}".format(str(requestor_student.id),str(requestor_student.grades),str(requestor_student.popularity)))

        for component in results:
            if component.__class__ is list:
                print("Component set OR:")
                for item in component:
                    self.__print_component(item)
            else:
                self.__print_component(component)
        
    def __print_component(self, component):
        string = ''
        if component.__class__ is Seat:
            string += "      Seat -- ID: {}, Row: {}, Col: {}".format(str(component.id),str(component.row),str(component.column))
        if component.__class__ is Student:
            string += "      Student -- ID: {}, Grades: {}, Popularity: {}".format(str(component.id),str(component.grades),str(component.popularity))
        print(string)