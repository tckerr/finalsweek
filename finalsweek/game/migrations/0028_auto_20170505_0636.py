# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0027_auto_20170504_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mutationtemplate',
            name='expiry_criteria',
        ),
        migrations.AlterField(
            model_name='mutationtemplate',
            name='gameflow_binding',
            field=models.CharField(choices=[('Phase', 'Phase'), ('Game', 'Game'), ('NextTurn', 'NextTurn'), ('Turn', 'Turn'), ('Stage', 'Stage')], max_length=255),
        ),
        migrations.AlterField(
            model_name='mutationtemplate',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Until Removed', 'Until Removed'), ('Draw', 'Draw'), ('Turn Bound', 'Turn Bound'), ('Status Effect', 'Status Effect'), ('Stage Bound', 'Stage Bound'), ('Phase Bound', 'Phase Bound'), ('Permanent', 'Permanent'), ('Draw After School Card', 'Draw After School Card'), ('Discipline Card', 'Discipline Card'), ('After School Card', 'After School Card'), ('Played Card', 'Played Card'), ('Trouble', 'Trouble'), ('Action Card Cost', 'Action Card Cost'), ('Automatic Card', 'Automatic Card'), ('Card Cost', 'Card Cost'), ('Trouble per Turn', 'Trouble per Turn'), ('System', 'System'), ('Grades per Turn', 'Grades per Turn'), ('Action Card', 'Action Card'), ('Popularity', 'Popularity'), ('Grades', 'Grades'), ('Proximate Effect', 'Proximate Effect'), ('After School Card Cost', 'After School Card Cost'), ('Automatic Effect', 'Automatic Effect'), ('Torment', 'Torment'), ('Draw Action Card', 'Draw Action Card'), ('Use Bound', 'Use Bound'), ('Actor Action', 'Actor Action'), ('Seat', 'Seat'), ('Card', 'Card')], max_length=381),
        ),
    ]