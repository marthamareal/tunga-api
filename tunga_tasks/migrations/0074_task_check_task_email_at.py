# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0073_auto_20170319_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='check_task_email_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
