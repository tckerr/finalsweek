# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 01:22
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_auto_20170428_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutationtemplate',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ActorAction', 'Actor Action'), ('AfterSchoolCard', 'After School Card'), ('ActionCard', 'Action Card'), ('ProximateEffect', 'Proximate Effect'), ('TurnBound', 'Turn Bound'), ('Grades', 'Grades'), ('Popularity', 'Popularity'), ('Card', 'Card'), ('ActionCardCost', 'Action Card Cost'), ('AfterSchoolCardCost', 'After School Card Cost'), ('Trouble', 'Trouble'), ('PhaseBound', 'Phase Bound'), ('Torment', 'Torment'), ('Permanent', 'Permanent'), ('StageBound', 'Stage Bound'), ('UntilRemoved', 'Until Removed'), ('DisciplineCard', 'Discipline Card'), ('PlayedCard', 'Played Card'), ('AutomaticCard', 'Automatic Card'), ('StatusEffect', 'Status Effect'), ('CardCost', 'Card Cost'), ('AutomaticEffect', 'Automatic Effect'), ('System', 'System'), ('OnDraw', 'On Draw'), ('UseBound', 'Use Bound')], max_length=284),
        ),
    ]
