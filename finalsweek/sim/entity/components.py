from django.db import models
from sim.messaging.message_types import MessageTypes
from django.contrib.auth.models import User
from datetime import datetime

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
    round_number = models.IntegerField(null=False)
    expended = models.DateTimeField(null=True)


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
    these are OPTIONS
    """
    #action_message = models.CharField(max_length=256)
    name = models.CharField(null=False, max_length=256)    
    uses = models.IntegerField(null=True) # null = infinite
    action_type = models.CharField(null=True, max_length=256) 
        # enum?
        # 1.  PlayActionCard
        # 2.  PlayAfterSchoolCard
        # 3.  PlayDisciplineCard ??
        # 4.  Draw
        # 5.  TargetOther
        # 6.  TargetSelf
        # 7.  TargetAllOthers
        # 8.  TargetAll
        # 9.  TargetSeat
        # 10. Confirm ??
        # 11. TargetDirection
        # 12. TargetAdjacent
        # 13. ChooseNumberInRange

        # alternate:
        # conditions:
        #   types (student, actor, seat, direction)
        #  TargetOther: count: 1, id != me, type=actor, type=student
        #  TargetSelf: count: 1 , id == me
        #  TargetAllOthers, id != me
        #  TargetAll, __all__
        #  TargetSeat

        # target:
        


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