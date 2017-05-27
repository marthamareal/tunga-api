# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 11:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0098_merge_20170526_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressreport',
            name='deadline_deliverable_rate',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='progressreport',
            name='next_deadline_meet',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='progressreport',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='progressreport',
            name='stuck_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='progressreport',
            name='stuck_reason',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='progressreport',
            name='today_to_dos',
            field=models.TextField(blank=True, null=True),
        ),
    ]
