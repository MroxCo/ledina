# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0027_auto_20170503_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='needs_edit',
            field=models.BooleanField(default=False),
        ),
    ]
