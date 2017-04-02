from django.core.management.base import BaseCommand
from sim.entity.filtering.target_strategy_builder import TargetStrategyBuilder
from sim.entity.filtering.util.target_strategy_printer import TargetStrategyPrinter
import json, os

class FilterTester(object):

    def test(self, path):    
        data = ''    
        with open(path, 'r', encoding='utf-8') as jsonfile:
            #json_str = jsonfile.read().replace('\n', '')
            #print(json_str)
            data = json.loads(jsonfile.read())

        builder = TargetStrategyBuilder()
        printer = TargetStrategyPrinter()
        root_strategy = builder.build(data)
        printer.print(root_strategy)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # now do the things that you want with your models here

        filter_tester = FilterTester()
        path = os.path.dirname(__file__) + '/fixtures/filter.json'
        filter_tester.test(path)