# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 22:23
from __future__ import unicode_literals

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0011_auto_20170428_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='mutationtemplate',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='mutationtemplate',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mutationtemplate',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[('system', 'System'), ('proximate_effect', 'ProximateEffect'), ('stage_bound', 'StageBound'),
                         ('permanent', 'Permanent'), ('popularity', 'Popularity'), ('turn_bound', 'TurnBound'),
                         ('discipline_card', 'DisciplineCard'), ('on_draw', 'OnDraw'), ('card', 'Card'),
                         ('automatic_effect', 'AutomaticEffect'), ('status_effect', 'StatusEffect'),
                         ('phase_bound', 'PhaseBound'), ('automatic_card', 'AutomaticCard'), ('trouble', 'Trouble'),
                         ('actor_action', 'ActorAction'), ('use_bound', 'UseBound'), ('action_card', 'ActionCard'),
                         ('until_removed', 'UntilRemoved'), ('card_cost', 'CardCost'), ('grades', 'Grades'),
                         ('afterschool_card_cost', 'AfterSchoolCardCost'), ('afterschool_card', 'AfterSchoolCard'),
                         ('torment', 'Torment'), ('played_card', 'PlayedCard')], max_length=287),
        ),
    ]
