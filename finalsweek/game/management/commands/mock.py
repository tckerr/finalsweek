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
        game_summary = self.router.load(self.actor_id)
        self.__assert_permissions(game_summary)
        if game_summary.complete:
            return False
        if game_summary.current_turn_actor_id == self.actor_id:
            self.__take_turn(game_summary)
        return True

    def __assert_permissions(self, game_summary):
        for actor_summary in game_summary.actors:
            assert actor_summary != self.actor_id
            assert getattr(actor_summary, "action_hand", None) is None
        assert game_summary.me.id == self.actor_id
        assert game_summary.me.action_hand is not None

    def __take_turn(self, game_summary):
        print("Actor {actor}'s turn is up. Stage: {stage}, Phase: {phase}".format(
                actor=str(self.actor_id), 
                stage=game_summary.stage, 
                phase=game_summary.phase))            
        if game_summary.phase == "Classtime":
            random_card = choice(PileCard.objects.filter(pile=game_summary.me.action_hand))
            action = UseActionCardAction(self.actor_id, random_card.card_id)
            print("   Using card id {}, pc: {}".format(str(random_card.card_id), str(random_card.id)))
            self.router.take_turn(self.actor_id, action)
        else:
            self.router.take_turn(self.actor_id)