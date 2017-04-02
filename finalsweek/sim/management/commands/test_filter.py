from django.core.management.base import BaseCommand
from sim.entity.filtering.target_strategy_builder import TargetStrategyBuilder
from sim.entity.filtering.target_strategy import ContextProvider
from sim.entity.filtering.util.target_strategy_printer import TargetStrategyPrinter
from sim.entity.filtering.util.test_classes import (Student, Seat)

import json, os

class JsonLoader(object):

    def load(self, path):
        with open(path, 'r', encoding='utf-8') as jsonfile:
            return json.loads(jsonfile.read())

        

class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.json_loader = JsonLoader()
        self.builder = TargetStrategyBuilder()
        self.printer = TargetStrategyPrinter()

    def handle(self, *args, **options):
        json_path = os.path.dirname(__file__) + '/fixtures/filter.json'        
        data = self.json_loader.load(json_path)      

        context_provider = ContextProvider()
        root_strategy = self.builder.build(data, context_provider)
        self.printer.print(root_strategy)

        results = root_strategy.evaluate()
        self.__print_results(results, context_provider)

    def __print_results(self, results, context_provider):
        print ("--- results ---")
        requestor_seat = context_provider.requestor_by_type(Seat)
        requestor_student = context_provider.requestor_by_type(Student)
        print("Requestor Seat -- ID: {}, Row: {}, Col: {}".format(str(requestor_seat.id),str(requestor_seat.row),str(requestor_seat.column)))
        print("Requestor Student ID: {}, Grades: {}, Pop: {}".format(str(requestor_student.id),str(requestor_student.grades),str(requestor_student.popularity)))
        for component_set in results:
            print("Component set:")
            for component in component_set:
                string = ''
                if component.__class__ is Seat:
                    string += "      Seat -- ID: {}, Row: {}, Col: {}".format(str(component.id),str(component.row),str(component.column))
                if component.__class__ is Student:
                    string += "      Student -- ID: {}, Grades: {}, Popularity: {}".format(str(component.id),str(component.grades),str(component.popularity))
                print(string)