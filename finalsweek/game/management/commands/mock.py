from django.core.management.base import BaseCommand
#
from game.game_tester import GameManager

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        router = GameManager()
        turn = router.create()

        while True:
            if turn:
                print("Stage: {}, Phase: {}, Actor {}'s turn".format(str(turn.phase.stage.stage_type_id), str(turn.phase.phase_type_id), str(turn.actor.id)))
                turn = router.take_turn(turn.actor.id)
            else:
                break
        print("Game over!")            