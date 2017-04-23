# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0011_card_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argument',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='cardtargetoperationset',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='operation',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='operationset',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]
