# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-16 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_app', '0006_auto_20180616_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaner',
            name='city',
            field=models.CharField(max_length=10),
        ),
    ]
