from django.core.management.base import BaseCommand
#
from sim.engine.initializer import Initializer
from sim.engine.savestate import Rules


class Command(BaseCommand):

    def handle(self, *args, **options):
        # now do the things that you want with your models here
       
        print("======================( Functional test )======================")
        initializer = Initializer.new([1, 2], Rules(5))
        initializer.mock()

        #print("======================( Performance test )======================")
        #initializer = Initializer.new([], Rules(100000))
        #initializer.performance_test()