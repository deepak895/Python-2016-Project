# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_auto_20170222_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='customer_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='job.Customer'),
            preserve_default=False,
        ),
    ]
