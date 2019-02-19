# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-19 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_payments', '0024_invoice_finalized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='credit_note_amount',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='send_credit_note',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.CharField(choices=[(b'sale', b'Sales Invoice'), (b'purchase', b'Purchase Invoice'), (b'client', b'Client'), (b'tunga', b'Tunga'), (b'developer', b'Developer'), (b'credit_nota', b'Credit Nota')], max_length=50),
        ),
    ]
