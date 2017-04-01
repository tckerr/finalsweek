from django.db import models

class RulesetFactory(object):

    def create(self, max_actors, actions_per_turn, auto_create_ai):
        ruleset = Ruleset()
        ruleset.max_actors = max_actors
        ruleset.actions_per_turn = actions_per_turn
        ruleset.auto_create_ai = auto_create_ai
        ruleset.save()
        return ruleset


class Ruleset(models.Model):

    max_actors = models.IntegerField(default=4)    
    actions_per_turn = models.IntegerField(default=2)    
    auto_create_ai = models.BooleanField(default=True)