from datetime import datetime

from django.core.management.base import BaseCommand

from trace import logger
from test_runner import TestRunner


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.test_runner = TestRunner()

    def handle(self, *args, **options):
        run_count = 50
        user_count = 4
        print("Starting stress test: {} runs for {} users.".format(run_count, user_count))
        start = datetime.utcnow()
        self.run_stress_test(run_count, user_count)
        elapsed = datetime.utcnow() - start
        print("Done! {} runs for {} users took {}s.".format(run_count, user_count, elapsed.total_seconds()))

    def run_stress_test(self, count, user_count):
        logger.enabled = False
        for current_run in range(1, 1 + count):
            start = datetime.utcnow()
            self.test_runner.run_create_test(user_count)
            elapsed = datetime.utcnow() - start
            print("> Finished run {} in {}s.".format(current_run, elapsed.total_seconds()))
