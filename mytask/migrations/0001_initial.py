# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='\u6211\u7684\u601d\u8def', max_length=20, verbose_name='\u601d\u8def\u540d\u79f0')),
                ('pubdate', models.DateTimeField(default=datetime.datetime(2014, 12, 9, 14, 53, 36, 645000), verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('content', models.TextField(default='\u6211\u7684\u601d\u8def\u662f\u3002\u3002\u3002', verbose_name='\u601d\u8def\u5185\u5bb9')),
                ('state', models.BooleanField(default=True, verbose_name='\u662f\u5426\u542f\u7528')),
                ('publisher', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u4efb\u52a1\u601d\u8def',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('pubdate', models.DateField(default=datetime.datetime(2014, 12, 9, 14, 53, 36, 645000), verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('content', models.TextField(default=b'Task is ....', verbose_name='\u4efb\u52a1\u5185\u5bb9')),
                ('level', models.CharField(default='\u6b63\u5e38', max_length=20, verbose_name='\u4efb\u52a1\u7ea7\u522b')),
                ('progress', models.IntegerField(default=0, verbose_name='\u4efb\u52a1\u8fdb\u5ea6')),
                ('is_fixed', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5b8c\u6210')),
                ('state', models.BooleanField(default=True, verbose_name='\u662f\u5426\u542f\u7528')),
                ('publisher', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u6211\u7684\u4efb\u52a1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u7c7b\u522b\u540d\u79f0')),
                ('state', models.BooleanField(default=True, verbose_name='\u662f\u5426\u542f\u7528')),
            ],
            options={
                'verbose_name_plural': '\u4efb\u52a1\u7c7b\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(to='mytask.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='mytask.Task'),
            preserve_default=True,
        ),
    ]
