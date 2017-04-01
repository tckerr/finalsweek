from datetime import datetime
from django.db import models

class Game(models.Model):
    class Meta:
        get_latest_by = 'created'

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(default=datetime.now)

    # rules
    ruleset = models.ForeignKey("Ruleset")
    