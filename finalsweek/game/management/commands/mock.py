from django.core.management.base import BaseCommand
#
from game.gameflow.game_router import GameRouter
from game.actions import UseActionCardAction
from random import choice
from game.models import PileCard

class Command(BaseCommand):

    def handle(self, *args, **options):
        player_count = 4
        router = GameRouter()
        game_info = router.create(player_count)
        ai = [RandomPollAi(actor, router) for actor in game_info.actors]

        while True:
            more = choice(ai).poll()
            if not more:
                break
        print("Game over!")



class RandomPollAi(object):
    def __init__(self, actor, router):
        self.actor = actor
        self.actor_id = actor.id
        self.router = router

    def poll(self):
        print("Actor {} polling for turn...".format(str(self.actor_id)))
        current_turn = self.router.load(self.actor_id).current_turn
        if not current_turn:
            return False
        if current_turn.actor.id == self.actor_id:
            self.__take_turn(current_turn)
        else:
            print("Not my turn.")
        return True

    def __take_turn(self, current_turn):
        print("Actor {actor}'s turn is up. Stage: {stage}, Phase: {phase}".format(
                actor=str(self.actor_id), 
                stage=str(current_turn.phase.stage.stage_type_id), 
                phase=str(current_turn.phase.phase_type_id)))            
        if current_turn.phase.phase_type_id == "Classtime":
            random_card = choice(PileCard.objects.filter(pile=self.actor.action_hand))
            action = UseActionCardAction(self.actor, random_card.card_id)
            print("   Using card id {}, pc: {}".format(str(random_card.card_id), str(random_card.id)))
            self.router.take_turn(self.actor_id, action)
        else:
            self.router.take_turn(self.actor_id)