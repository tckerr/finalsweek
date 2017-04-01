from django.db import models
from sim.messaging.message_types import MessageTypes
from django.contrib.auth.models import User

class Component(models.Model):
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey("Entity")

    def __init__(self, *args, **kwargs):
        super(Component, self).__init__(*args, **kwargs)

    # extend me
    def msg(self, message_type, data):
        if message_type is MessageTypes.DebugEcho:
            print("Echoing from {}:".format(str(self.id)), data["value"])

        if message_type is MessageTypes.DebugValues:
            class_name = self.__class__.__name__
            print("Echoing from {}({}):".format(class_name, str(self.id)), self.__dict__)


class IntegerComponent(Component):
    class Meta:
        abstract = True

    value = models.IntegerField(default=0)

    def add(self, value):
        self.value += value
        self.save()

    def remove(self, value):
        self.add(-1 * value)
        self.save()

class PopularityComponent(IntegerComponent):
    pass

class TurnComponent(Component):
    '''
    has turn counter, gets += 1 each turn
    player with turn counter = total players goes next and it gets set to 0
    if player leaves, all --1
    '''    
    actions_left = models.IntegerField(null=False)

class GradesComponent(IntegerComponent):
    def msg(self, message_type, data):
        if message_type is MessageTypes.GradesModification:
            self.add(data["value"])

        if message_type is MessageTypes.ReportGrades:
            print(self.value)

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
    #action_message = models.CharField(max_length=256)

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
    user = models.ForeignKey(User, null=True)
    gameslot_number = models.IntegerField(null=True)

    def msg(self, message_type, data):
        if message_type is MessageTypes.UpdateGameslot:
            self.gameslot_number = data["value"]
            self.save()

        super(ActorComponent, self).msg(message_type, data)

    def is_ai(self):
        return self.user_id is None