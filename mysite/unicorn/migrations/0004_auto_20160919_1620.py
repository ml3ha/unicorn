# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicorn', '0003_auto_20160919_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='school',
            field=models.CharField(choices=[('SEAS', 'School of Engineering and Applied Sciences'), ('BATTEN', 'Frank Batten School of Leadership and Public Policy'), ('CLAS', 'College of Arts and Sciences'), ('CURRY', 'Curry School of Education'), ('Darden', 'Darden School of Business'), ('COMM', 'McIntire School of Commerce'), ('SARC', 'School of Architecture'), ('SCPS', 'School of Continuing and Professional Studies'), ('LAW', 'School of Law'), ('MED', 'School of Medicine'), ('NURSE', 'School of Nursing')], max_length=1),
        ),
    ]
