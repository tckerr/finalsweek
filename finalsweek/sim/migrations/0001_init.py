# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 02:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
