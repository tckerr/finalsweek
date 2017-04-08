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


class Actor(DefaultModel):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", related_name="actors")
    user = models.ForeignKey(User, related_name="player_actors", null=True)
    student_info = models.ForeignKey("StudentInfo", related_name="+")
    discard_pile = models.ForeignKey("Pile", related_name="+")
    action_hand = models.ForeignKey("Pile", related_name="+")
    afterschool_hand = models.ForeignKey("Pile", related_name="+")
    grades = models.IntegerField()
    popularity = models.IntegerField()

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
    name = models.CharField(max_length=255)
    piles = models.ManyToManyField("Pile", through="PileCard", related_name="cards")

class PileCard(DefaultModel):
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    pile = models.ForeignKey("Pile", on_delete=models.CASCADE)

# card effects ---------------

class EntityType(DefaultModel):
    id = models.CharField(max_length=255, primary_key=True)

class EffectSet(DefaultModel):
    def __str__(self):
       effect_list = [str(eff) for eff in self.effects.all()]
       return "Set: {}".format(", ".join(effect_list))

    id = models.AutoField(primary_key=True)


class Effect(DefaultModel):
    def __str__(self):
       return "{}".format(self.description) 
    id = models.AutoField(primary_key=True)
    effect_sets = models.ManyToManyField("EffectSet", related_name="effects")
    description = models.CharField(max_length=255)
    eligible_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

class Target(DefaultModel):

    def __str__(self):
       return "{}".format(self.description)  

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    sift = models.TextField()
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

class CardTargetEffectSet(DefaultModel):
    def __str__(self):
        return "CARD {} --> TARGETS {} --> WITH EFFECTS {}".format(
            str(self.card),
            str(self.target),
            str(self.effect_set)) 

    id = models.AutoField(primary_key=True)
    card = models.ForeignKey("Card", related_name="card_target_effect_sets", on_delete=models.CASCADE)
    effect_set = models.ForeignKey("EffectSet", related_name="+", on_delete=models.CASCADE)
    target = models.ForeignKey("Target", related_name="+", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.__target_result_type_equality():
            raise Exception("You may not create a CardTargetEffectSet set that has differing target types between the target result and effect type.")
        super(CardTargetEffectSet, self).save(*args, **kwargs)

    def __target_result_type_equality(self):
        expected_type = self.target.target_content_type
        for effect in self.effect_set.effects.all():
            if effect.eligible_content_type is not expected_type:
                return False
        return True