# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0005_auto_20160102_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_details',
            name='board_number',
        ),
        migrations.AddField(
            model_name='company_details',
            name='board_number_1',
            field=models.CharField(default='-', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_details',
            name='board_number_2',
            field=models.CharField(default='-', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='designation',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
