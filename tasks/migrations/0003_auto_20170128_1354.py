# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_last_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='max_repeat_factor',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='task',
            name='repeat_factor',
            field=models.PositiveIntegerField(default=7),
        ),
    ]
