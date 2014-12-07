# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PwdHelper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=200, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88')),
                ('state', models.BooleanField(default=True, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8')),
            ],
            options={
                'verbose_name_plural': '\u5bc6\u7801\u5e2e\u52a9',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PwdQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('que_content', models.CharField(default=b'', max_length=30, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81\xe9\x97\xae\xe9\xa2\x98')),
                ('state', models.BooleanField(default=True, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8')),
            ],
            options={
                'verbose_name_plural': '\u5bc6\u7801\u95ee\u9898',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pwdhelper',
            name='question',
            field=models.ForeignKey(to='accounts.PwdQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pwdhelper',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
