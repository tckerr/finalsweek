# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0017_card_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='script',
            field=models.TextField(blank=True, default=''),
        ),
    ]
