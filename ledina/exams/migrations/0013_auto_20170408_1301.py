# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_exam_exam_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_file',
            field=models.FileField(upload_to=''),
        ),
    ]
