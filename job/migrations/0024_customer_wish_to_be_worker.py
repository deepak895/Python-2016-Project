# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0023_auto_20170227_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='wish_to_be_worker',
            field=models.BooleanField(default=False),
        ),
    ]
