from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class DefaultModel(models.Model):
    class Meta:
        abstract = True


    created = models.DateTimeField(default=timezone.now)


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


class CardType(DefaultModel):
    def __str__(self):
        return "{}".format(self.id)

    id = models.CharField(max_length=255, primary_key=True)


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


class Game(DefaultModel):
    id = models.CharField(primary_key=True, max_length=255)


class Participant(DefaultModel):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
