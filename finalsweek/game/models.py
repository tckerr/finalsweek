from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

from game.configuration.definitions import Tag


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
    mutation_template = models.ForeignKey("MutationTemplate", related_name="+", null=True)


class Game(DefaultModel):
    id = models.CharField(primary_key=True, max_length=255)


class Participant(DefaultModel):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)


'''

MutationTemplate describes how a mutation is created. If Card.mutation_template is not 
    null, this means it does not get discarded but goes into play afterward. It will 
    use the MutationTemplate to create an InPlayEffect under the actor by 1) building 
    a Mutation from a MutationTemplate, 2) inserting that mutation into the game's
    mutation list, and 3) setting the InPlayEffect on the player
`
Mutation = actual thing making the changes
MutationTemplate = used by a Card when played to create the Mutation and InPlayEffect 
MutationExpiryCriteria: describes when a mutation expires
InPlayEffect = thing owned by actor that links mutation to a card (this is what Mutation is currently)

When an operation is created, it sets the
'''


class OperationModifier(DefaultModel):
    def __str__(self):
        return self.id

    id = models.CharField(primary_key=True, max_length=255)
    script = models.TextField(default="", blank=True)
    active = models.BooleanField(default=True)


class MutationExpiryCriteria(DefaultModel):
    id = models.AutoField(primary_key=True)


class OperationTag(DefaultModel):
    def __str__(self):
        return self.name

    name = models.CharField(primary_key=True, max_length=255)


class MutationTemplate(DefaultModel):
    def __str__(self):
        return self.name or "undefined"

    # source_actor_id = models.BooleanField(default=False)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    tags = MultiSelectField(choices=Tag.tag_list())
    priority = models.IntegerField(default=0)

    # can be used if we want
    match_all = models.BooleanField(default=False)

    # need to create this on the mutation class
    expiry_criteria = models.ForeignKey(MutationExpiryCriteria, null=True)  # null = permanent

    # currently mutation_effect_id on the resulting Mutation (we're renaming mutation effect to OperationModifier)
    operation_modifier = models.ForeignKey(OperationModifier)
