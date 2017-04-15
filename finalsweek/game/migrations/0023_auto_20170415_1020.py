# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0022_auto_20170415_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='actor',
        ),
        migrations.AddField(
            model_name='actor',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='game.Student'),
        ),
    ]