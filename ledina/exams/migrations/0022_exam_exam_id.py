# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0021_remove_exam_exam_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
