# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='last_complete',
            field=models.DateTimeField(default='1970-01-01 00:00:00'),
        ),
    ]
