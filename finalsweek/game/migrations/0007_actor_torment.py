# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0006_actor_trouble'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='torment',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
