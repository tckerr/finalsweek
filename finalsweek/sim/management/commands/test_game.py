from django.core.management.base import BaseCommand
#
from sim.engine.game_interface import DebugGameInterface
from sim.testing.game_mocker import GameMocker
from sim.models import Game

class Command(BaseCommand):

    def handle(self, *args, **options):
        # now do the things that you want with your models here

        mocker = GameMocker()
        game_interface = DebugGameInterface()
        ruleset_id = game_interface.create_ruleset(10, 3, 5, True)

        print("======================( New test )======================")
        newgame_manager = game_interface.create_game_debug([], 5, ruleset_id)
        mocker.mock(newgame_manager)

        print("======================( Load test )======================")
        loaded_manager = game_interface.load_game(Game.objects.latest().id)
        mocker.mock(loaded_manager)

        print("======================( Turn test )======================")
        newgame_manager = game_interface.create_game_debug([], 5, ruleset_id)
        mocker.turn_test(newgame_manager)

        #print("======================( Performance test )======================")
        #initializer = Initializer.new([], Rules(100000))
        #initializer.performance_test()