#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from procedure_article.models import Article



# Create your models here.

class Type(models.Model):
    name = models.CharField(u'类别名称', max_length=20 , null=False)
    state = models.BooleanField(u'是否启用' , default=True , null=False)
    
    def __unicode__(self):
        return self.name 
    
    def show(self):
        return self.objects.filter(state=True)
    
    class Meta:
        verbose_name_plural = '任务类别'
    
class Task(models.Model):
    publisher = models.ForeignKey(User)
    type = models.ForeignKey(Type)
    
    name = models.CharField(u'任务名称' , max_length=20 , null=False)
    pubdate = models.DateField(u'发布日期' , null=False , default=datetime.today())
    content = models.TextField(u'任务内容' , null=False , default='Task is ....')
    level = models.CharField(u'任务级别' , max_length=20 , null=False , default=u'正常')
    progress = models.IntegerField(u'任务进度' , null=False , default=0)
    is_fixed = models.BooleanField(u'是否完成' , null=False , default=False)
    state = models.BooleanField(u'是否启用', null=False , default=True)
    
    def __unicode__(self):
        return self.name 
    
    # show 
    def show(self):
        return self.objects.filter(state=True)
    
    class Meta:
        verbose_name_plural = '我的任务'
    

class Comment(models.Model):
    publisher = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    
    name = models.CharField(u'思路名称' , max_length=20 , null=False , default=u'我的思路')
    pubdate = models.DateTimeField(u'发布时间' , null=False , default=datetime.now())
    content = models.TextField(u'思路内容' , null=False , default=u'我的思路是。。。')
    state = models.BooleanField(u'是否启用' , null=False , default=True)

    def __unicode__(self):
        return self.name
    
    def show(self): 
        return  self.objects.filter(state=True)
    
    class Meta:
        verbose_name_plural = '任务思路'
    
    
        
    
    
    
    
    
    
    
