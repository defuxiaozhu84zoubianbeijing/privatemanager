#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib.auth.models import User
from django import forms
from crispy_forms.bootstrap import  FormActions, PrependedText
from crispy_forms.helper import Layout , FormHelper
from crispy_forms.layout import Submit, HTML
from accounts.models import PwdQuestion , PwdHelper

# 登陆
class loginForm(forms.ModelForm):
    username = forms.CharField(
        label=u'用户名',
        max_length=20 ,
        required=True,
    )
    
    password = forms.CharField(
        label=u'密码' ,
        max_length=20,
        widget=forms.PasswordInput() ,
        required=True,
    )
    
    remember_me = forms.BooleanField(
        label=u'记住我' ,
        widget=forms.CheckboxInput(),
        required=False,
        
    )
    
    class Meta:
        model = User 
        fields = ['username' , 'password' , 'remember_me']
        
    def __init__(self , *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-5'
        self.helper.layout = Layout(
            'username' ,
            'password' ,
            'remember_me',
            FormActions(
                Submit('btn_login', u'登陆', css_class='btn-default'),
                HTML(u'<a href="/accounts/getpwd/">找回密码</a>') 
            ),
                                  
        )
# 注册      
class registerForm(forms.ModelForm):
    username = forms.CharField(
        label=u'用户名',
        max_length=20 ,
        required=True,
    )
    
    password = forms.CharField(
        label=u'密码',
        max_length=20,
        widget=forms.PasswordInput() ,
        required=True,
    )
    
    email = forms.CharField(
        label=u'邮箱',
        max_length=200 ,
        required=True,
    )
    
    question = forms.ModelChoiceField(
        label=u'找回问题' ,
        empty_label=u'请选择问题' ,
        queryset=PwdQuestion.objects.filter(state=True),
        to_field_name='id' ,
    )
    
    answer = forms.CharField(
        label=u'问题答案',
        max_length=30 ,
        required=True                       
    )
    
    class Meta:
        model = User 
        fields = ['username' , 'password' , 'email' , 'question' , 'answer' ]
        
    def __init__(self , *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-5'
        self.helper.layout = Layout(
            'username' ,
            'password' ,
            PrependedText('email', 'www.', placeholder=u'邮箱'),
            'question',
            'answer',
            FormActions(
                Submit('btn_login', u'注册', css_class='btn-default'),
            ),
        )

# 密码找回Form
class PwdHelperForm(forms.ModelForm): 
    email = forms.CharField(
        label=u'邮箱',
        max_length=200 ,
        required=True,
    ) 
    
    question = forms.ModelChoiceField(
        label=u'找回问题' ,
        empty_label=u'请选择问题' ,
        queryset=PwdQuestion.objects.filter(state=True),
        to_field_name='id' ,
    )
    
    answer = forms.CharField(
        label=u'问题答案',
        max_length=30 ,
        required=True                       
    )
    
    is_agress = forms.BooleanField(
        label=u'同意<a href="#">私人管家注册协议</a>' ,
        widget=forms.CheckboxInput(),
        required=True,
    )
    
    class Meta :
        model = PwdHelper
        fields = [ 'email' , 'question' , 'answer' , 'is_agress']
        
    def __init__(self , *args, **kwargs):
        super(PwdHelperForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-5'
        self.helper.layout = Layout(
            'email' ,
            'question' ,
            'answer' ,
            'is_agress',
            FormActions(
                Submit('btn_login', u'找回', css_class='btn-default'),
            ),
        )
        
# 修改密码
class PassWordChangeForm(forms.ModelForm):
    oldPwd = forms.CharField(
        label=u'原始密码' ,
        max_length=30 ,
        widget=forms.PasswordInput() ,
        required=True ,
    )
    
    oldPwd_confirm = forms.CharField(
        label=u'确认密码',
        max_length=30 ,
        widget=forms.PasswordInput() ,
        required=True,
    )
    
    password = forms.CharField(
        label=u'新密码',
        max_length=30 ,
        widget=forms.PasswordInput() ,
        required=True,
    )
    
    class Meta:
        model = User 
        fields = ['oldPwd' , 'oldPwd_confirm' , 'password']
        
    def __init__(self , *args, **kwargs):
        super(PassWordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-5'
        self.helper.layout = Layout(
            'oldPwd' ,
            'oldPwd_confirm' ,
            'password' ,
            FormActions(
                Submit('btn_login', u'重置密码', css_class='btn-default'),
            ),
        )
    
    
