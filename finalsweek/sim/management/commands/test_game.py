from django.core.management.base import BaseCommand
#
from sim.engine.initializer import Initializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        # now do the things that you want with your models here
        
        initializer = Initializer()
        initializer.mock()
        initializer.performance_test()