# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 23:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0030_auto_20170507_0923'),
    ]

    database_operations = [
        migrations.AlterModelTable('Card', 'configuration_card'),
        migrations.AlterModelTable('MutationTemplate', 'configuration_mutationtemplate'),
        migrations.AlterModelTable('CardType', 'configuration_cardtype'),
        migrations.AlterModelTable('Participant', 'configuration_participant'),
        migrations.AlterModelTable('OperationModifier', 'configuration_operationmodifier'),
        migrations.AlterModelTable('OperationTag', 'configuration_operationtag'),
        migrations.AlterModelTable('StudentInfo', 'configuration_studentinfo'),
        migrations.AlterModelTable('Game', 'configuration_game'),
        migrations.AlterModelTable('DefaultModel', 'configuration_defaultmodel')
    ]

    state_operations = [
        migrations.DeleteModel('Card'),
        migrations.DeleteModel('MutationTemplate'),
        migrations.DeleteModel('CardType'),
        migrations.DeleteModel('Participant'),
        migrations.DeleteModel('OperationModifier'),
        migrations.DeleteModel('OperationTag'),
        migrations.DeleteModel('StudentInfo'),
        migrations.DeleteModel('Game'),
        migrations.DeleteModel('DefaultModel')
    ]

    database_operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]