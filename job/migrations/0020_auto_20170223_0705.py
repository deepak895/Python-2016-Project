# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_auto_20170223_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_end_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
