# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'python study', max_length=200, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('jianjie', models.CharField(default=b'python study', max_length=200, null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b')),
                ('keyword', models.CharField(default=b'python ', max_length=20, null=True, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('content', models.TextField(default=b'python study', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('author', models.CharField(default=b'wangxin', max_length=40, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('publishdate', models.DateField(default=datetime.datetime(2014, 11, 28, 10, 41, 16, 528000), verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('state', models.BooleanField(default=True, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8')),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe6\x88\x91\xe7\x9a\x84\xe8\xaf\x84\xe8\xae\xba', max_length=200, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(default=b'python study', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('author', models.CharField(default=b'wangxin', max_length=40, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('publishdate', models.DateField(default=datetime.datetime(2014, 11, 28, 10, 41, 16, 529000), verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('state', models.BooleanField(default=True, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8')),
                ('article', models.ForeignKey(to='procedure_article.Article')),
            ],
            options={
                'verbose_name_plural': '\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'python study', max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0')),
                ('parentId', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe7\xbc\x96\xe5\x8f\xb7')),
                ('parentName', models.CharField(default=b'Python', max_length=50, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('state', models.BooleanField(default=True, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8')),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(to='procedure_article.Type'),
            preserve_default=True,
        ),
    ]
