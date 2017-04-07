from django.core.management.base import BaseCommand
#
from game.game_router import GameRouter
from random import randint



class Command(BaseCommand):

    def handle(self, *args, **options):
        player_count = 4
        router = GameRouter()
        game_info = router.create(player_count)
        ai = [RandomPollAi(actor.id) for actor in game_info.actors]

        while True:
            actor = randint(0,3)
            more = ai[actor].poll()
            if not more:
                break
        print("Game over!")


class RandomPollAi(object):
    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.router = GameRouter()

    def poll(self):
        print("Actor {} polling for turn...".format(str(self.actor_id)))
        current_turn = self.router.load(self.actor_id).current_turn
        if not current_turn:
            return False
        if current_turn.actor.id == self.actor_id:
            print("Actor {actor}'s turn is up. Stage: {stage}, Phase: {phase}".format(
                actor=str(self.actor_id), 
                stage=str(current_turn.phase.stage.stage_type_id), 
                phase=str(current_turn.phase.phase_type_id)))
            self.router.take_turn(self.actor_id)
        else:
            print("Not my turn.")
        return True