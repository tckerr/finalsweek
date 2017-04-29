# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 21:07
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0025_auto_20170429_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutationtemplate',
            name='expiry_criteria',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Action Bound', 'Action Bound'), ('Permanent', 'Permanent'), ('Use Bound', 'Use Bound'), ('Phase Bound', 'Phase Bound'), ('Stage Bound', 'Stage Bound'), ('Until Removed', 'Until Removed'), ('Turn Bound', 'Turn Bound')], max_length=81),
        ),
        migrations.AlterField(
            model_name='mutationtemplate',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Played Card', 'Played Card'), ('Action Card Cost', 'Action Card Cost'), ('Trouble', 'Trouble'), ('After School Card', 'After School Card'), ('System', 'System'), ('Torment', 'Torment'), ('After School Card Cost', 'After School Card Cost'), ('Card Cost', 'Card Cost'), ('Proximate Effect', 'Proximate Effect'), ('Action Card', 'Action Card'), ('Phase Bound', 'Phase Bound'), ('Draw Action Card', 'Draw Action Card'), ('Discipline Card', 'Discipline Card'), ('Status Effect', 'Status Effect'), ('Draw', 'Draw'), ('Card', 'Card'), ('Draw After School Card', 'Draw After School Card'), ('Permanent', 'Permanent'), ('Grades per Turn', 'Grades per Turn'), ('Trouble per Turn', 'Trouble per Turn'), ('Use Bound', 'Use Bound'), ('Automatic Card', 'Automatic Card'), ('Automatic Effect', 'Automatic Effect'), ('Grades', 'Grades'), ('Actor Action', 'Actor Action'), ('Stage Bound', 'Stage Bound'), ('Until Removed', 'Until Removed'), ('Turn Bound', 'Turn Bound'), ('Popularity', 'Popularity')], max_length=376),
        ),
    ]
