# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0020_exam_exam_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_id',
        ),
    ]