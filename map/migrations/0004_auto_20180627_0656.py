# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-27 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_parameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='upload_file',
            field=models.FileField(blank=True, upload_to='upload_files'),
        ),
    ]
