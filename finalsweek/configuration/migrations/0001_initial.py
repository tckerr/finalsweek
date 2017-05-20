# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 23:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0031_auto_20170519_1946')
    ]

    state_operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(default='')),
                ('script', models.TextField(blank=True, default='')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('trouble_cost', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
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
                ('name', models.CharField(default='', max_length=255)),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('StatAdd', 'StatAdd'), ('Action Card', 'Action Card'), ('Stage Bound', 'Stage Bound'), ('Turn Bound', 'Turn Bound'), ('Until Removed', 'Until Removed'), ('Played Card', 'Played Card'), ('Discipline Card', 'Discipline Card'), ('StatSubtract', 'StatSubtract'), ('Torment', 'Torment'), ('Grades', 'Grades'), ('Seat', 'Seat'), ('Trouble', 'Trouble'), ('Card Cost', 'Card Cost'), ('Use Bound', 'Use Bound'), ('After School Card', 'After School Card'), ('Proximate Effect', 'Proximate Effect'), ('Card', 'Card'), ('Draw After School Card', 'Draw After School Card'), ('System', 'System'), ('Grades per Turn', 'Grades per Turn'), ('Automatic Effect', 'Automatic Effect'), ('Status Effect', 'Status Effect'), ('Trouble per Turn', 'Trouble per Turn'), ('Draw Action Card', 'Draw Action Card'), ('Phase Bound', 'Phase Bound'), ('Actor Action', 'Actor Action'), ('Permanent', 'Permanent'), ('Draw', 'Draw'), ('Action Card Cost', 'Action Card Cost'), ('Popularity', 'Popularity'), ('Automatic Card', 'Automatic Card'), ('After School Card Cost', 'After School Card Cost')], max_length=402)),
                ('priority', models.IntegerField(default=0)),
                ('uses', models.IntegerField(default=None, null=True)),
                ('match_all', models.BooleanField(default=False)),
                ('gameflow_binding', models.CharField(choices=[('Next After School Phase', 'Next After School Phase'), ('Next Choose Seats Phase', 'Next Choose Seats Phase'), ('Next Accumulation Phase', 'Next Accumulation Phase'), ('Next Score Phase', 'Next Score Phase'), ('Game', 'Game'), ('Phase', 'Phase'), ('Turn', 'Turn'), ('Stage', 'Stage'), ('Next Classtime Phase', 'Next Classtime Phase'), ('Next Dismissal Phase', 'Next Dismissal Phase')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperationModifier',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('script', models.TextField(blank=True, default='')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperationTag',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('backstory', models.CharField(max_length=255)),
                ('perk_name', models.CharField(max_length=255)),
                ('perk_description', models.TextField()),
                ('fear_name', models.CharField(max_length=255)),
                ('fear_description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mutationtemplate',
            name='operation_modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.OperationModifier'),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='configuration.CardType'),
        ),
        migrations.AddField(
            model_name='card',
            name='mutation_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='configuration.MutationTemplate'),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
