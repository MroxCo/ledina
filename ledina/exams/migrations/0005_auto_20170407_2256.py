# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-07 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20170407_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='number',
            new_name='exam_number',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='path',
            new_name='exam_path',
        ),
    ]