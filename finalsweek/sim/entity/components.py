from sim.messaging.message_types import MessageTypes

class Component(object):

    def __init__(self, id_delegate):
        self.id = id_delegate()

    # overwrite me
    def receive_message(self, message_type, data):
        pass

class IntegerComponent(Component):

    def __init__(self, *args, **kwargs):
        self.__value = 0
        super(IntegerComponent, self).__init__(*args, **kwargs)

    def add(self, value):
        self.__value += value

    def remove(self, value):
        self.add(-1 * value)

    @property
    def value(self):
        return self.__value


class PopularityComponent(IntegerComponent): pass
class TurnComponent(Component):
    '''
    has turn counter, gets += 1 each turn
    player with turn counter = total players goes next and it gets set to 0
    if player leaves, all --1
    '''

class GradesComponent(IntegerComponent):
    def receive_message(self, message_type, data):
        if message_type is MessageTypes.GradesModification:
            self.add(data["value"])

        if message_type is MessageTypes.ReportGrades:
            print self.value

# cards

class CostComponent(Component):
    """
    Emits a resource expense message when it receives a played message
    This could be a "turn" cost for cards
    """

class DisposableComponent(Component):
     """
    Emits a discard message when it receives a played message
    defines target pile
    """

class ActionComponent(Component):
    """
    Is a candidate for action on a turn
    defines the action
    """

class StackableComponent(Component):
    """
    Can be held in a pile (deck, hand)
    """

class VisibilityComponent(Component):
    """
    public - all can see
    private - hidden from other players than sibling obsever
    unknown - hidden to all but system
    """
