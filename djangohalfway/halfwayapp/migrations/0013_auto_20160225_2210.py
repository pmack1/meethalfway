# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halfwayapp', '0012_auto_20160225_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='business_type',
            field=models.TextField(blank=True, null=True),
        ),
    ]