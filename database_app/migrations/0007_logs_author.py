# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0006_auto_20160109_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='author',
            field=models.CharField(default='admin', max_length=30),
            preserve_default=False,
        ),
    ]
