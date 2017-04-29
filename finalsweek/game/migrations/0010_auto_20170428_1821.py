# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 22:21
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20170428_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mutationtemplate',
            name='tags',
        ),
        migrations.AlterField(
            model_name='mutationtemplate',
            name='tags2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('until_removed', 'UntilRemoved'), ('stage_bound', 'StageBound'), ('trouble', 'Trouble'), ('automatic_effect', 'AutomaticEffect'), ('afterschool_card', 'AfterSchoolCard'), ('afterschool_card_cost', 'AfterSchoolCardCost'), ('turn_bound', 'TurnBound'), ('card', 'Card'), ('torment', 'Torment'), ('system', 'System'), ('proximate_effect', 'ProximateEffect'), ('action_card', 'ActionCard'), ('grades', 'Grades'), ('card_cost', 'CardCost'), ('use_bound', 'UseBound'), ('phase_bound', 'PhaseBound'), ('status_effect', 'StatusEffect'), ('played_card', 'PlayedCard'), ('discipline_card', 'DisciplineCard'), ('permanent', 'Permanent'), ('on_draw', 'OnDraw'), ('popularity', 'Popularity'), ('automatic_card', 'AutomaticCard'), ('actor_action', 'ActorAction')], max_length=287),
        ),
    ]