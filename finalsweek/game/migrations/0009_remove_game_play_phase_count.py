# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0008_auto_20170410_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='play_phase_count',
        ),
    ]
