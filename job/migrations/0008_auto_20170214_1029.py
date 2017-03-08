# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_estimation'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Estimate_Cost',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to='job.Estimation'),
        ),
        migrations.AlterField(
            model_name='estimation',
            name='extra_cost',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AlterField(
            model_name='estimation',
            name='total_cost',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AlterField(
            model_name='estimation',
            name='trasportation_charge',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AlterField(
            model_name='estimation',
            name='visit_charge',
            field=models.FloatField(default=0.0, max_length=100),
        ),
    ]