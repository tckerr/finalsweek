# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0002_auto_20170401_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='turncomponent',
            name='expended',
            field=models.IntegerField(default=False),
        ),
    ]
