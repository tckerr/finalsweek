# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 22:29
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_auto_20170428_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutationtemplate',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('TurnBound', 'Turn Bound'), ('UntilRemoved', 'Until Removed'), ('Grades', 'Grades'), ('AutomaticCard', 'Automatic Card'), ('OnDraw', 'On Draw'), ('Trouble', 'Trouble'), ('CardCost', 'Card Cost'), ('Card', 'Card'), ('ActionCard', 'Action Card'), ('ActorAction', 'Actor Action'), ('Permanent', 'Permanent'), ('DisciplineCard', 'Discipline Card'), ('AfterSchoolCard', 'After School Card'), ('StageBound', 'Stage Bound'), ('PhaseBound', 'Phase Bound'), ('System', 'System'), ('AutomaticEffect', 'Automatic Effect'), ('PlayedCard', 'Played Card'), ('StatusEffect', 'Status Effect'), ('AfterSchoolCardCost', 'After School Card Cost'), ('UseBound', 'Use Bound'), ('Torment', 'Torment'), ('ProximateEffect', 'Proximate Effect'), ('Popularity', 'Popularity')], max_length=269),
        ),
    ]