# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0023_auto_20170415_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pile',
            name='requires_type',
        ),
        migrations.RemoveField(
            model_name='pile',
            name='size_limit',
        ),
    ]
