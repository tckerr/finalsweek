from django.core.management.base import BaseCommand
#
from game.gameflow.game_router import GameRouter
from game.actions import UseActionCardAction
from random import choice
from game.models import PileCard
from game.options import ResultSet
from siftpy._choice import Choice

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
        self.decider = Decider()

    def poll(self):
        #print("Actor {} polling for turn...".format(str(self.actor_id)))
        game_summary = self.router.load(self.actor_id)
        self.__assert_permissions(game_summary)
        if game_summary.complete:
            return False
        if game_summary.current_turn_actor_id == self.actor_id:
            options = self.router.get_turn_options(self.actor_id, {})            
            self.__take_turn(game_summary, options)
        return True

    def __assert_permissions(self, game_summary):
        for actor_summary in game_summary.actors:
            assert actor_summary != self.actor_id
            assert getattr(actor_summary, "action_hand", None) is None
        assert game_summary.me.id == self.actor_id
        assert game_summary.me.action_hand is not None

    def __take_turn(self, game_summary, options):
        print("Actor {actor}'s turn is up. Stage: {stage}, Phase: {phase}".format(
                actor=str(self.actor_id), 
                stage=game_summary.stage, 
                phase=game_summary.phase))            
        if game_summary.phase == "Classtime":
            print("My options:", options)
            decisions = self.decider.decide(options)
            print("My decisions:", decisions)
            self.router.take_turn_desc(self.actor_id, decisions)
        else:
            self.router.take_turn(self.actor_id)

from random import randint

class Decider(object):

    def decide(self, turn_choices):
        card_choice = choice(list(turn_choices.keys()))
        decisions = {"card_id": card_choice}
        for card_id, card_choices in turn_choices.items():
            decisions[card_id] = {}
            for cto_id, cto_choices in card_choices.items():
                decisions[card_id][cto_id] = {
                    "target_decisions": [],
                    "operation_set_decisions": {}
                }
                for item in cto_choices["target_choices"]:                    
                    if self.__is_choice(item):
                        random_choice = self.__random_choice(item)
                        decisions[card_id][cto_id]["target_decisions"].append(random_choice)
                    else:
                        decisions[card_id][cto_id]["target_decisions"].append(item)
                        
                for operation_id, operation_choices in cto_choices["operation_set_choices"].items():
                    decisions[card_id][cto_id]["operation_set_decisions"][operation_id] = {}
                    for arg_id, argument_choices in operation_choices.items():
                        decisions[card_id][cto_id]["operation_set_decisions"][operation_id][arg_id] = []
                        for item in argument_choices:                    
                            if self.__is_choice(item):
                                random_choice = self.__random_choice(item)
                                decisions[card_id][cto_id]["operation_set_decisions"][operation_id][arg_id].append(random_choice)
                            else:
                                decisions[card_id][cto_id]["operation_set_decisions"][operation_id][arg_id].append(item)
        return decisions



    def __is_choice(self, obj):
        # NEED BETTER WAY
        return obj.__class__ is Choice

    def __random_choice(self, choice):
        count = len(choice.question)
        return randint(0, count-1)
