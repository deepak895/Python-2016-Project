# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_admin_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_request', models.CharField(default='', max_length=200)),
                ('service_dateTime', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='Reg_date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='services_request',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Customer'),
        ),
    ]
