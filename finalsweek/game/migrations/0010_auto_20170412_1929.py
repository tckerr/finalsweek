# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_remove_game_play_phase_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtargetoperationset',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operationset',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]