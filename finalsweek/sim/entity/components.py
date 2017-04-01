from django.db import models
from sim.messaging.message_types import MessageTypes

class ComponentIdGenerator(object):
    __component_incr = 0

    @classmethod
    def generate(cls):
        cls.__component_incr += 1
        return cls.__component_incr


class Component(models.Model):
    class Meta:
        abstract = True

    def __init__(self):
        self.id = ComponentIdGenerator.generate()

    # extend me
    def msg(self, message_type, data):
        if message_type is MessageTypes.DebugEcho:
            print "Echoing from {}:".format(str(self.id)), data["value"]

        if message_type is MessageTypes.DebugValues:
            class_name = self.__class__.__name__
            print "Echoing from {}({}):".format(class_name, str(self.id)), self.__dict__


class IntegerComponent(Component):
    class Meta:
        abstract = True

    value = models.IntegerField(default=0)

    def add(self, value):
        self.value += value

    def remove(self, value):
        self.add(-1 * value)



class PopularityComponent(IntegerComponent):
    pass

class TurnComponent(Component):
    '''
    has turn counter, gets += 1 each turn
    player with turn counter = total players goes next and it gets set to 0
    if player leaves, all --1
    '''

class GradesComponent(IntegerComponent):
    def msg(self, message_type, data):
        if message_type is MessageTypes.GradesModification:
            self.add(data["value"])

        if message_type is MessageTypes.ReportGrades:
            print self.value

        super(GradesComponent, self).msg(message_type, data)

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

class ActorComponent(Component):
    def __init__(self, *args, **kwargs):
        super(ActorComponent, self).__init__(*args, **kwargs)
        self.user_id = None
        self.seat_id = None

    def is_ai(self):
        return self.user_id is None

