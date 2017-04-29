# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170426_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutationExpiryCriteria',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MutationTemplate',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.IntegerField(default=0)),
                ('match_all', models.BooleanField(default=False)),
                ('system', models.BooleanField(default=False)),
                ('actor_action', models.BooleanField(default=False)),
                ('status_effect', models.BooleanField(default=False)),
                ('automatic_effect', models.BooleanField(default=False)),
                ('card', models.BooleanField(default=False)),
                ('discipline_card', models.BooleanField(default=False)),
                ('afterschool_card', models.BooleanField(default=False)),
                ('action_card', models.BooleanField(default=False)),
                ('played_card', models.BooleanField(default=False)),
                ('automatic_card', models.BooleanField(default=False)),
                ('afterschool_card_cost', models.BooleanField(default=False)),
                ('card_cost', models.BooleanField(default=False)),
                ('proximate_effect', models.BooleanField(default=False)),
                ('on_draw', models.BooleanField(default=False)),
                ('turn_bound', models.BooleanField(default=False)),
                ('phase_bound', models.BooleanField(default=False)),
                ('stage_bound', models.BooleanField(default=False)),
                ('use_bound', models.BooleanField(default=False)),
                ('until_removed', models.BooleanField(default=False)),
                ('permanent', models.BooleanField(default=False)),
                ('popularity', models.BooleanField(default=False)),
                ('grades', models.BooleanField(default=False)),
                ('trouble', models.BooleanField(default=False)),
                ('torment', models.BooleanField(default=False)),
                ('target_actor_id', models.BooleanField(default=False)),
                ('source_actor_id', models.BooleanField(default=False)),
                ('expiry_criteria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.MutationExpiryCriteria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='MutationEffect',
            new_name='OperationModifier',
        ),
        migrations.AddField(
            model_name='mutationtemplate',
            name='operation_modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.OperationModifier'),
        ),
        migrations.AddField(
            model_name='card',
            name='mutation_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.MutationTemplate'),
        ),
    ]