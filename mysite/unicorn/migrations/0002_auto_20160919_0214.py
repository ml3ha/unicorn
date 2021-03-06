# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('unicorn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='headshot',
            field=models.ImageField(blank=True, null=True, upload_to='headshots'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
