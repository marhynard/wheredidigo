# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitparser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='activityspeed',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='fileinfo',
            name='activitytype',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='filename',
            field=models.CharField(max_length=75, unique=True),
        ),
    ]
