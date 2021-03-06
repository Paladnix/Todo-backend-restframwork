# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='down',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='expire',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, default=b'ToDo', max_length=32),
        ),
    ]
