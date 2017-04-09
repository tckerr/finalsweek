from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
'''
Create Game
Subscribe Actors --> ref a StudentInfo and maybe a User
Create a Round
Create a Turn
    accumulate Turn Histories, each time "complete" turn if player is done
    check if round is done if a turn ends
    if not, create new Turn
    if so, complete round

    Game > Stage > Phase > Round > Turns
"Finals week" > "Play Stage" > "Action Phase" > "Round 2" > "Tom's Turn"
    
'''

class DefaultModel(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(default=timezone.now)


class Game(DefaultModel):
    id = models.AutoField(primary_key=True)
    play_phase_count = models.IntegerField()
    action_deck = models.ForeignKey("Pile", related_name="+")
    afterschool_deck = models.ForeignKey("Pile", related_name="+")
    discipline_card_deck = models.ForeignKey("Pile", related_name="+")

class StageType(DefaultModel):
    id = models.CharField(max_length=255, primary_key=True)
    '''
        GameStart
        Play
        Scoring
    '''
class Stage(DefaultModel):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", related_name="stages")
    completed = models.DateTimeField(null=True)
    stage_type = models.ForeignKey("StageType", related_name="+")

class PhaseType(DefaultModel):
    id = models.CharField(max_length=255, primary_key=True)
    '''
        GameStart
            Choose Seats ?
        Play
            Accumulation
            Classtime
            Dismissal
            After School
        Scoring
            Score
    '''
    stage_type = models.ForeignKey("StageType", related_name="+")
    is_automatic = models.BooleanField()
    # Assert that a phase's stage's stage_type = that phase's phasetype's stage_type

class Phase(DefaultModel):
    id = models.AutoField(primary_key=True)
    stage = models.ForeignKey("Stage", related_name="phases")
    completed = models.DateTimeField(null=True)
    phase_type = models.ForeignKey("PhaseType", related_name="+")

class Turn(DefaultModel):
    id = models.AutoField(primary_key=True)
    actor = models.ForeignKey("Actor", related_name="turns") 
    phase = models.ForeignKey("Phase", related_name="turns")
    completed = models.DateTimeField(null=True)


class StudentInfo(DefaultModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    backstory = models.CharField(max_length=255)

class Pile(DefaultModel):
    id = models.AutoField(primary_key=True)
    size_limit = models.IntegerField(null=True)
    requires_type = models.ForeignKey("Pile", related_name="+", null=True)

    def add_card(self, card):
        pc = PileCard()
        pc.card = card
        pc.pile = self
        pc.save()

class Seat(DefaultModel):
    id = models.AutoField(primary_key=True)
    row = models.IntegerField()
    column = models.IntegerField()
    game = models.ForeignKey("Game", related_name="seats")

    @property
    def empty(self):
        return self.actor_or_none is None

    @property
    def actor_or_none(self):
        try:
            return self.actor
        except:
            return None


class Actor(DefaultModel):
    def __str__(self):
       return "Actor: {}".format(self.id)

    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", related_name="actors")
    user = models.ForeignKey(User, related_name="player_actors", null=True)
    student_info = models.ForeignKey("StudentInfo", related_name="+")
    discard_pile = models.ForeignKey("Pile", related_name="+")
    action_hand = models.ForeignKey("Pile", related_name="+")
    afterschool_hand = models.ForeignKey("Pile", related_name="+")
    seat = models.OneToOneField("Seat", related_name="actor")
    grades = models.IntegerField()
    popularity = models.IntegerField()
    torment = models.IntegerField()
    trouble = models.IntegerField()

class CardType(DefaultModel):
    def __str__(self):
       return "{}".format(self.id)

    id = models.CharField(max_length=255, primary_key=True)
    '''
    AfterSchool
    Action
    Discipline
    '''

class Card(DefaultModel):
    def __str__(self):
       return "{} ({})".format(self.name, str(self.id))

    id = models.AutoField(primary_key=True)
    card_type = models.ForeignKey("CardType", related_name="+")
    name = models.CharField(max_length=255, unique=True)
    piles = models.ManyToManyField("Pile", through="PileCard", related_name="cards")

class PileCard(DefaultModel):
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    pile = models.ForeignKey("Pile", on_delete=models.CASCADE)

# card operations ---------------

class EntityType(DefaultModel):
    id = models.CharField(max_length=255, primary_key=True)

class OperationSet(DefaultModel):
    def __str__(self):
       operation_list = [str(eff) for eff in self.operations.all()]
       return "Set: {}".format(", ".join(operation_list))

    id = models.AutoField(primary_key=True)

class Operator(DefaultModel):
    def __str__(self):
       return "{}".format(self.id) 
    id = models.CharField(max_length=255, primary_key=True)

class Operation(DefaultModel):
    def __str__(self):
        args = ", ".join([a.description for a in self.arguments.all()])
        return "{} {}".format(str(self.instruction), args) 

    id = models.AutoField(primary_key=True)
    operation_set = models.ForeignKey("OperationSet", related_name="operations", on_delete=models.CASCADE)
    instruction = models.ForeignKey("Instruction", related_name="operations", on_delete=models.CASCADE)    
    arguments = models.ManyToManyField("Argument", related_name="operations") # set?

class Instruction(DefaultModel):
    def __str__(self):
       return "{}".format(self.description) 

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    eligible_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_field = models.CharField(max_length=255)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

# RENAME TO ARG, MOVE TO M2M with operation/operation set 
class Argument(DefaultModel):
    def __str__(self):
       return "{}={}".format(self.key,self.description) 

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    is_sift = models.BooleanField() # potentially move this to its own table
    key = models.CharField(max_length=255)
    value = models.TextField()
    # TODO: add type

class Target(DefaultModel):

    def __str__(self):
       return "{}".format(self.description)  

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    sift = models.TextField()
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

class CardTargetOperationSet(DefaultModel):
    def __str__(self):
        return "CARD {} --> TARGETS {} --> WITH OPERATIONS {}".format(
            str(self.card),
            str(self.target),
            str(self.operation_set)) 

    id = models.AutoField(primary_key=True)
    card = models.ForeignKey("Card", related_name="card_target_operation_sets", on_delete=models.CASCADE)
    operation_set = models.ForeignKey("OperationSet", related_name="+", on_delete=models.CASCADE)
    target = models.ForeignKey("Target", related_name="+", on_delete=models.CASCADE)
    execution_order = models.IntegerField() 

    def save(self, *args, **kwargs):
        if not self.__target_result_type_equality:
            raise Exception("You may not create a CardTargetOperationSet set that has differing target types between the target result and operation type.")
        super(CardTargetOperationSet, self).save(*args, **kwargs)

    @property
    def __target_result_type_equality(self):
        expected_type = self.target.target_content_type
        for operation in self.operation_set.operations.all():
            if operation.instruction.eligible_content_type != expected_type:
                return False
        return True