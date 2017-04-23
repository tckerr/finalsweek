
from django.core.management.base import BaseCommand

from game.test_runner import TestRunner


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.test_runner = TestRunner()

    def handle(self, *args, **options):
        self.test_runner.run_create_test(4)
