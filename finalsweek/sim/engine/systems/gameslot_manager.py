import random
from sim.entity.providers import ActorProvider
from sim.messaging.message_types import MessageTypes
from sim.messaging.message import ValueMessage

class Table(object):
    def __init__(self, size):
        self.size = size

    @property
    def gameslots(self):
        return [seat_number for seat_number in range(0, self.size)]

class GameslotManager(object):
    #TODO: make this not based on actors
    def __init__(self, game):
        self.actor_provider = ActorProvider(game)
        self.table = Table(game.ruleset.max_actors)
    
    def jumble(self):
        gameslots = self.__jumble_list(self.table.gameslots)
        actor_components = self.__jumble_list(self.actor_provider.all)
        for actor_component in actor_components:
            gameslots_number = gameslots.pop()
            actor_component.msg(MessageTypes.UpdateGameslot, ValueMessage(gameslots_number))

    def __jumble_list(self, val):
        new_val = list(val)
        random.shuffle(new_val)
        return new_val