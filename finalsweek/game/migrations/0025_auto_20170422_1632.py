# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20170417_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='action_hand',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='afterschool_hand',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='discard_pile',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='game',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='student',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='game',
            name='action_deck',
        ),
        migrations.RemoveField(
            model_name='game',
            name='afterschool_deck',
        ),
        migrations.RemoveField(
            model_name='game',
            name='discipline_card_deck',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='phase_type',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='phasetype',
            name='stage_type',
        ),
        migrations.RemoveField(
            model_name='pilecard',
            name='card',
        ),
        migrations.RemoveField(
            model_name='pilecard',
            name='pile',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='game',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='game',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='stage_type',
        ),
        migrations.DeleteModel(
            name='StageType',
        ),
        migrations.RemoveField(
            model_name='student',
            name='seat',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_info',
        ),
        migrations.RemoveField(
            model_name='turn',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='turn',
            name='phase',
        ),
        migrations.RemoveField(
            model_name='card',
            name='piles',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Phase',
        ),
        migrations.DeleteModel(
            name='PhaseType',
        ),
        migrations.DeleteModel(
            name='Pile',
        ),
        migrations.DeleteModel(
            name='PileCard',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
        migrations.DeleteModel(
            name='Stage',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Turn',
        ),
    ]