# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_utils', '0022_searchevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchevent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
