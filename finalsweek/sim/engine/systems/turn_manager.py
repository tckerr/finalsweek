from sim.entity.components import TurnComponent
from sim.entity.providers import ActorProvider
from sim.exceptions import GameFlowViolation
import random
from datetime import datetime
from django.utils import timezone


class TurnManager(object):

    #TODO: make this not based on actors

    def __init__(self, game):
        self.game = game    
        self.actor_provider = ActorProvider(self.game)
        self.components = TurnComponent.objects

    def provide_turn(self):        
        actor_components = list(self.actor_provider.all)
        turns_this_game = list(self.components.filter(entity__game=self.game))
        current_round = 0
        if turns_this_game:            
            current_round = max([turn.round_number for turn in turns_this_game])
            actors_gone_this_round = len(list(filter(lambda turn: turn.expended is not None and turn.round_number == current_round, turns_this_game)))
            if len(actor_components) <= actors_gone_this_round:
                current_round += 1
        if current_round <= self.game.ruleset.rounds_per_game:
            self.__initialize_next_turn(current_round) 
        else:
            raise Exception("Game over, man!")

    def expend_action(self, entity, cost):
        if not self.__entity_has_turn(entity):
            raise GameFlowViolation("It is not this entity's turn.")

        turn_component = self.__pending_for_entity(entity.id).first()
        turn_component = self.__save_turn_details(cost, turn_component)

        if self.__turn_is_complete(turn_component):
            self.__conclude_turn(entity)

    # --- private --- 

    def __initialize_next_turn(self, round_number):
        if not self.__needs_turn_assignment():
            return
        # TODO: check for phase change
        actor_components = list(self.actor_provider.all)
        next_gameslot = self.__get_next_gameslot(actor_components)            
        next_actor = self.__get_actor_for_gameslot(actor_components, next_gameslot)
        self.__assign_turn(next_actor.entity, round_number)        
    
    def __needs_turn_assignment(self):
        return self.components.filter(entity__game=self.game, expended__isnull=True).count() <= 0

    def __entity_has_turn(self, entity):
        count = self.__pending_for_entity(entity.id).count()
        return count > 0
      
    def __get_actor_for_gameslot(self, actor_components, next_gameslot):
        for actor in actor_components:
            if actor.gameslot_number == next_gameslot:
                return actor

    def __get_next_gameslot(self, actor_components):
        min_gameslot = self.__get_min_gameslot_number(actor_components)
        if self.__there_has_been_at_least_one_turn():            
            most_recent_actor_to_take_turn = self.__get_actor_with_most_recent_turn(actor_components)
            most_recent_slot = most_recent_actor_to_take_turn.gameslot_number
            return self.__get_next_valid_gameslot(most_recent_slot, actor_components) or min_gameslot
        else:
            return min_gameslot

    def __get_min_gameslot_number(self, actor_components):
        return min([actor.gameslot_number for actor in actor_components])

    def __get_next_valid_gameslot(self, previous_number, actor_components):
        valids = [actor.gameslot_number for actor in actor_components if actor.gameslot_number > previous_number]
        if valids:
            return min(valids)            

    def __there_has_been_at_least_one_turn(self):
        return self.components.filter(entity__game=self.game, expended__isnull=False).count() > 0

    def __get_max_gameslot_among_actors(self, actor_components):
        return max([actor.gameslot_number for actor in actor_components])

    def __get_actor_with_most_recent_turn(self, actor_components):
        actor_maximum_expended_turn = []
        for actor_component in actor_components:
            entity = actor_component.entity
            turns = self.__expended_for_entity(entity.id)
            if turns:
                most_recent_actor_turn = max([turn.expended for turn in turns])
                actor_maximum_expended_turn.append((actor_component, most_recent_actor_turn))
        most_recent_turn_overall = sorted(actor_maximum_expended_turn, key=lambda turns: turns[1], reverse=True)[0]
        return most_recent_turn_overall[0]

    def __conclude_turn(self, entity):
        if not self.__entity_has_turn(entity):
            raise GameFlowViolation("It is not this entity's turn.")
        component = self.__pending_for_entity(entity.id).first()
        component.expended = timezone.now()
        component.save()


    def __expended_for_entity(self, entity_id):
        return self.components.filter(**{
            'expended__isnull': False,
            'entity__game': self.game,
            'entity_id': entity_id
        })

    def __pending_for_entity(self, entity_id):
        return self.components.filter(**{
            'expended__isnull': True,
            'entity__game': self.game,
            'entity_id': entity_id
        })

    def __save_turn_details(self, cost, turn_component):
        if not self.__has_enough_actions(cost, turn_component):
            exception_text = "This entity does not have enough actions. (cost: {}, actions_left: {})"
            raise GameFlowViolation(exception_text.format(str(cost), str(turn_component.actions_left)))

        turn_component.actions_left -= cost        
        turn_component.save()
        return turn_component
        
    def __assign_turn(self, entity, round_number):
        if self.__entity_has_turn(entity):
            raise Exception("This entity already has a turn.")
        turn_component = TurnComponent()
        turn_component.entity_id = entity.id
        turn_component.round_number = round_number
        turn_component.expended = None
        turn_component.actions_left = self.game.ruleset.actions_per_turn
        turn_component.save()

    def __turn_is_complete(self, turn_component):
        return turn_component.actions_left <= 0

    def __has_enough_actions(self, cost, turn_component):
        return turn_component.actions_left >= cost

    