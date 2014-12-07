# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('procedure_article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keyword',
            field=models.CharField(default=b'python ', max_length=200, null=True, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publishdate',
            field=models.DateField(default=datetime.datetime(2014, 11, 30, 9, 39, 1, 189000), verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publishdate',
            field=models.DateField(default=datetime.datetime(2014, 11, 30, 9, 39, 1, 189000), verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
