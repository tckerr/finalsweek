import random
from sim.entity.providers import ActorProvider
from sim.messaging import MessageTypes, ValueMessage

class Table(object):
    def __init__(self, size):
        self.size = size

    @property
    def seats(self):
        return [seat_number for seat_number in range(0, self.size)]

class SeatManager(object):

    def __init__(self, component_entity_map, rules):
        self.actor_provider = ActorProvider(component_entity_map)
        self.table = Table(rules.total_actors)
    
    def jumble(self):
        seats = self.__jumble_list(self.table.seats)
        actor_components = self.__jumble_list(self.actor_provider.all)
        for actor_component in actor_components:
            seat_number = seats.pop()
            actor_component.msg(MessageTypes.UpdateSeat, ValueMessage(seat_number))

    def __jumble_list(self, val):
        new_val = list(val)
        random.shuffle(new_val)
        return new_val