# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_total_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_voter',
            field=models.IntegerField(default=0),
        ),
    ]