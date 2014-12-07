#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 密码问题类
class PwdQuestion(models.Model):
    que_content = models.CharField('密码问题', max_length=30 , null=False , default='')
    state = models.BooleanField('启用', null=False , default=True)
    
    def __unicode__(self):
        return self.que_content
    
    class Meta:
        verbose_name_plural = '密码问题'
    


# 密码找回帮助类
class PwdHelper(models.Model):
    user = models.OneToOneField(User)
    question = models.ForeignKey(PwdQuestion)
    answer = models.CharField('答案' , max_length=200 , null=False)
    state = models.BooleanField('启用' , null=False , default=True)
    
    def __unicode__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = '密码帮助'
    

