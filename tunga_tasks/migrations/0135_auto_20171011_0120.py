# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-11 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0134_workactivity_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='payment_link_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='payment_link_sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]