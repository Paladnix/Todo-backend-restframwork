# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20171009_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='down',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]