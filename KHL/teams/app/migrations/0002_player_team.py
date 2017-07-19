# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-16 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='app.Team'),
            preserve_default=False,
        ),
    ]
