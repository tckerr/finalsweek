# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 20:42
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='argument',
            name='instruction',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='operation_sets',
        ),
        migrations.AddField(
            model_name='operation',
            name='argument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations',
                                    to='game.Argument'),
        ),
        migrations.AddField(
            model_name='operation',
            name='instuction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations',
                                    to='game.Instruction'),
        ),
        migrations.AddField(
            model_name='operation',
            name='operation_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations',
                                    to='game.OperationSet'),
        ),
    ]
