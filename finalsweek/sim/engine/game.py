from datetime import datetime
from django.db import models

class Game(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(default=datetime.now)

    # rules
    total_actors = models.IntegerField()    
    auto_create_ai = models.BooleanField(default=True)
