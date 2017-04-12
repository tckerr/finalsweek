from django.core.management.base import BaseCommand
#
from game.interface.routers import GameRouter
from game.actions import UseActionCardAction
from random import choice
from game.models import PileCard
from siftpy._choice import Choice
from pprint import pprint

class Command(BaseCommand):

    def handle(self, *args, **options):
        player_count = 5
        router = GameRouter()
        game_info = router.create(player_count)
        ai = [RandomPollAi(actor, router) for actor in game_info.actors]

        while True:
            #more = choice(ai).poll()
            current_turn = router.load(ai[0].actor_id)
            more = list(filter(lambda act: act.actor_id == current_turn.current_turn_actor_id, ai))
            if not more:
                break
            more[0].poll()
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
            print("My options:")
            pprint(options)
            decisions = self.decider.decide(options)
            print("My decisions:")
            pprint(decisions)
            self.router.take_turn(self.actor_id, decisions)
        else:
            self.router.take_turn(self.actor_id, {})

from random import randint

class Decider(object):

    def decide(self, turn_options):
        actioncard_options = turn_options["Action Cards"]
        card_choice = choice(list(actioncard_options.keys()))
        card_options = actioncard_options[card_choice]
        decisions = {
            "Action Cards": {
                card_choice: self.__decide_card(card_options)
            }
        }
        decisions["card_name"] = card_choice
        return decisions


    def __decide_card(self, card_options):
        card_decisions = {}
        if not card_options:
            return card_decisions
        for cto_id, _ in card_options.items():
            card_decisions[cto_id] = {
                "target_decisions": [],
                "operation_set_decisions": {}
            }
            if card_options[cto_id] and card_options[cto_id]["target_choices"]:
                for item in card_options[cto_id]["target_choices"]:                    
                    if self.__is_choice(item):
                        random_choice = self.__random_choice(item)
                        card_decisions[cto_id]["target_decisions"].append(random_choice)
                    else:
                        card_decisions[cto_id]["target_decisions"].append(item)

            if card_options[cto_id] and card_options[cto_id]["operation_set_choices"]:       
                for operation_id, operation_choices in card_options[cto_id]["operation_set_choices"].items():
                    card_decisions[cto_id]["operation_set_decisions"][operation_id] = {}
                    if not operation_choices:
                        continue
                    for arg_id, argument_choices in operation_choices.items():
                        card_decisions[cto_id]["operation_set_decisions"][operation_id][arg_id] = []
                        if not argument_choices:
                            continue
                        for item in argument_choices:                    
                            if self.__is_choice(item):
                                random_choice = self.__random_choice(item)
                                card_decisions[cto_id]["operation_set_decisions"][operation_id][arg_id].append(random_choice)
                            else:
                                card_decisions[cto_id]["operation_set_decisions"][operation_id][arg_id].append(item)
        return card_decisions

    def __decide_cto(self, cto_options):
        pass
        


    def __is_choice(self, obj):
        # NEED BETTER WAY
        return obj.__class__ is Choice

    def __random_choice(self, choice):
        print("Choosing randomly from:")
        pprint(choice.question)
        count = len(choice.question)
        return randint(0, count-1)
