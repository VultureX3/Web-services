# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-16 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
