from django.core.management.base import BaseCommand

from test_runner import TestRunner


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.test_runner = TestRunner()

    def handle(self, *args, **options):
        game_id = options['game_id'][0]
        actor_id = options['actor_id'][0]
        self.test_runner.run_load_test(game_id, actor_id)

    def add_arguments(self, parser):
        parser.add_argument('game_id', nargs='+', type=str)
        parser.add_argument('actor_id', nargs='+', type=str)
