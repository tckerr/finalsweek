# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0004_auto_20170401_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruleset',
            name='rounds_per_game',
            field=models.IntegerField(default=10),
        ),
    ]