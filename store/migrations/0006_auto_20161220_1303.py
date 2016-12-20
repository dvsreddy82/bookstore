# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20161220_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='payment_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookorder',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
