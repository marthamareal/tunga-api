# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-09 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0065_workplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]