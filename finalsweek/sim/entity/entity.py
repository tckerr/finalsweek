from django.db import models

class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", related_name="entities")
