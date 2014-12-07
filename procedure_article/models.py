#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    
    name = models.CharField('类别名称' , max_length=50 , null=False , default='python study')
    parentId = models.IntegerField('上级编号', null=False , default=0)
    parentName = models.CharField('上级名称', max_length=50 , null=False , default='Python')
    state = models.BooleanField('启用' , null=False , default=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '文章分类'
        
class Article(models.Model):
    type = models.ForeignKey(Type)
    
    title = models.CharField('文章标题' , max_length=200 , null=False , default='python study')
    jianjie = models.CharField('文章简介' , max_length=200, null=True , default='python study')
    keyword = models.CharField('关键字'  , max_length=200 , null=True , default='python ')
    content = models.TextField('内容' , null=False, default='python study')
    author = models.CharField('作者' , max_length=40 , default='wangxin')
    publishdate = models.DateField('发布时间' , null=False , default=datetime.today())
    state = models.BooleanField('启用' , null=False , default=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta :
        verbose_name_plural = '文章'
        
class Comment(models.Model):
    article = models.ForeignKey(Article)
    title = models.CharField('评论标题' , max_length=200 , null=False , default='我的评论')
    content = models.TextField('评论内容' , null=False , default='python study')
    author = models.CharField('作者' , max_length=40 , default='wangxin')
    publishdate = models.DateField('发布时间' , null=False , default=datetime.today())
    state = models.BooleanField('启用' , null=False , default=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta :
        verbose_name_plural = '评论'
    
    
    
    
