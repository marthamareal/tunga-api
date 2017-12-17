# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-29 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_auth', '0012_auto_20171123_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='tungauser',
            name='payoneer_signup_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='tungauser',
            name='payoneer_status',
            field=models.CharField(choices=[(b'initial', 'Initial'), (b'approved', 'Approved'), (b'declined', 'Decline')], default=b'initial', help_text='initial - Initial, approved - Approved, declined - Decline', max_length=20),
        ),
    ]