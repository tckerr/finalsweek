# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0003_auto_20170408_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='instuction',
            new_name='instruction',
        ),
    ]
