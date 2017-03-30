# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0080_auto_20170325_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[(b'initial', 'Initial'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')], default=b'initial', help_text='initial - Initial,accepted - Accepted,rejected - Rejected', max_length=20),
        ),
        migrations.AddField(
            model_name='participation',
            name='status',
            field=models.CharField(choices=[(b'initial', 'Initial'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')], default=b'initial', help_text='initial - Initial,accepted - Accepted,rejected - Rejected', max_length=20),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='status',
            field=models.CharField(choices=[(b'initial', 'Initial'), (b'submitted', 'Submitted'), (b'approved', 'Approved'), (b'declined', 'Declined'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')], default=b'initial', help_text='initial - Initial, submitted - Submitted, approved - Approved, declined - Declined, accepted - Accepted, rejected - Rejected', max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(choices=[(b'initial', 'Initial'), (b'submitted', 'Submitted'), (b'approved', 'Approved'), (b'declined', 'Declined'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')], default=b'initial', help_text='initial - Initial, submitted - Submitted, approved - Approved, declined - Declined, accepted - Accepted, rejected - Rejected', max_length=20),
        ),
    ]
