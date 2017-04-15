# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_auto_20170415_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='perk_description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='perk_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]