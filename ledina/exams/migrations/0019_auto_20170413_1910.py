# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0018_auto_20170413_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examfile',
            old_name='file',
            new_name='exam_file',
        ),
    ]
