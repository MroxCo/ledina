# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0013_auto_20170408_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
