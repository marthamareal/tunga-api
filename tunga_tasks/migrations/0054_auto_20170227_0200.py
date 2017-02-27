# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-27 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0053_auto_20170227_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='email',
        ),
        migrations.AlterField(
            model_name='task',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
