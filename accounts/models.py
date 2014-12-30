#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
        verbose_name_plural = u'密码帮助'
        
class UserProfile(models.Model):
    
    user = models.OneToOneField(User, related_name='profile')
    duoshuo_id = models.IntegerField(default=0)
    token = models.IntegerField(default=0)
    avatar = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username
    
        

def create_user_profile(sender=None, instance=None, created=False, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
        userprofile.save()
models.signals.post_save.connect(create_user_profile, sender=User)
    

