from sim.entity.components import TurnComponent
from sim.entity.providers import ActorProvider
from sim.exceptions import GameFlowViolation
import random

class TurnManager(object):

    #TODO: make this not based on actors

    def __init__(self, game):
        self.game = game    
        self.actor_provider = ActorProvider(self.game)
        self.components = TurnComponent.objects

    def initialize_next_turn(self):
        # random for now
        actors = list(self.actor_provider.all)
        random.shuffle(actors)
        self.__assign_turn(actors[0].entity)
    
    def needs_turn_assignment(self):
        return self.components.filter(entity__game=self.game).count() <= 0

    def entity_has_turn(self, entity):
        return self.components.filter(entity_id=entity.id, entity__game=self.game).count() > 0

    def expend_action(self, entity, cost):
        if not self.entity_has_turn(entity):
            raise GameFlowViolation("It is not this entity's turn.")

        turn_component = TurnComponent.objects.get(entity_id=entity.id, entity__game=self.game)
        if self.__has_enough_actions(cost, turn_component):
            turn_component.actions_left -= cost
            turn_component.save()
        else:            
            exception_text = "This entity does not have enough actions. (cost: {}, actions_left: {})"
            raise GameFlowViolation(exception_text.format(str(cost), str(turn_component.actions_left)))

        if self.__turn_is_complete(turn_component):
            self.conclude_turn(entity)

    def conclude_turn(self, entity):
        if not self.entity_has_turn(entity):
            raise GameFlowViolation("It is not this entity's turn.")
        self.components.filter(entity_id=entity.id, entity__game=self.game).delete()
        
    def __assign_turn(self, entity):
        if self.entity_has_turn(entity):
            raise Exception("This entity already has a turn.")
        turn_component = TurnComponent()
        turn_component.entity_id = entity.id
        turn_component.actions_left = self.game.ruleset.actions_per_turn
        turn_component.save()

    def __turn_is_complete(self, turn_component):
        return turn_component.actions_left <= 0

    def __has_enough_actions(self, cost, turn_component):
        return turn_component.actions_left >= cost

    