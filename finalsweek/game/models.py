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
    def __str__(self):
       return self.name

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    backstory = models.CharField(max_length=255)
    perk_name = models.CharField(max_length=255)
    perk_description = models.TextField()
    fear_name = models.CharField(max_length=255)
    fear_description = models.TextField()

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

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
    def coordinates_str(self):
        return "({}, {})".format(self.column, self.row)

    @property
    def empty(self):
        try:
            return self.student is None
        except:
            return True

class Student(DefaultModel):

    def __init__(self, *a, **k):
        super(Student, self).__init__(*a, **k)

    def __str__(self):
       return "Student {}: {}".format(self.id, self.student_info)

    id = models.AutoField(primary_key=True)
    seat = models.OneToOneField("Seat", related_name="student")
    student_info = models.ForeignKey("StudentInfo", related_name="+")

    @property
    def controlled(self):
        return self.actor_or_none is not None

    @property
    def actor_or_none(self):
        try:
            return self.actor
        except:
            return None

class Actor(DefaultModel):
    def __str__(self):
       return "Actor {}: [{}]".format(self.id, self.student)

    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", related_name="actors")
    user = models.ForeignKey(User, related_name="player_actors", null=True)
    discard_pile = models.ForeignKey("Pile", related_name="+")
    action_hand = models.ForeignKey("Pile", related_name="+")
    afterschool_hand = models.ForeignKey("Pile", related_name="+")
    grades = models.IntegerField()
    popularity = models.IntegerField()
    torment = models.IntegerField()
    trouble = models.IntegerField()
    student = models.OneToOneField("Student", related_name="actor", null=True)

    @property
    def summary(self):
        return "[ Grades: {grades}, Pop: {popularity}, Troub: {trouble}, Tor: {torment}, Student Seat: {coords}]".format(
            grades=self.grades,
            popularity=self.popularity,
            trouble=self.trouble,
            torment=self.torment,
            coords=self.student.seat.coordinates_str)

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
       return "{} ({}): {}".format(self.name, str(self.id), self.description)

    id = models.AutoField(primary_key=True)
    card_type = models.ForeignKey("CardType", related_name="+")
    description = models.TextField(default="")
    script = models.TextField(default="", blank=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=True)
    trouble_cost = models.IntegerField(default=0)
    piles = models.ManyToManyField("Pile", through="PileCard", related_name="cards")

class PileCard(DefaultModel):
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    pile = models.ForeignKey("Pile", related_name="pile_cards", on_delete=models.CASCADE)
