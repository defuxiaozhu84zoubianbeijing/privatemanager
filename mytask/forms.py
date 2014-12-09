#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from mytask.models import Task , Comment , Type
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import InlineCheckboxes, FormActions

class TaskForm(forms.ModelForm):
    LEVEL_CHOICES = (
        ('搁置', '搁置'), ('正常', '正常'),
        ('紧急', '紧急'), ('立刻', '立刻'),
    )
    
    PROGRESS_CHOICES = (
        ('0', '0'), ('10', '10'), ('20', '20'),
        ('30', '30'), ('40', '40'), ('50', '50'),
        ('60', '60'), ('70', '70'), ('80', '80'),
        ('90', '90'), ('100', '100'),
    )

    # name
    name = forms.CharField(
        label=u'任务名称',
        max_length=20 ,
        required=True ,
        error_messages={'required': u'请输入任务名称', 'error':u'任务名称输入太长，请精简'},
    )
    # 文章类型 
    type = forms.ModelChoiceField(
        label=u'类型 ',
        empty_label=u'请选择文章类别' ,
        queryset=Type.objects.filter(state=True),
        to_field_name='id',
        required=True ,
        error_messages={'required': u'请选择任务类型'},
    )
    # 关键字
    level = forms.ChoiceField(
        label=u'任务级别',
        choices=LEVEL_CHOICES,
        error_messages={'required': u'请选择任务级别'},
        required=True,
    )  
    progress = forms.ChoiceField(
        label=u'任务进度',
        choices=PROGRESS_CHOICES,
        error_messages={'required': u'请选择任务进度'},
        required=True,
    )
    is_fixed = forms.BooleanField(
        label=u'是否结束',
        required=False,
    )
    # 文章内容
    content = forms.Textarea()

    class Meta:
        model = Task
        fields = [ 'name' , 'type', 'level' , 'progress', 'content' , 'is_fixed' ]
        
        
    def __init__(self , *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'name',
            'type' ,
            'level',
            'progress' ,
            'content',
            'is_fixed',
            FormActions(
                Submit('save', u'保存'),
            )
        )

class CommentForm(forms.ModelForm):
    content = forms.Textarea()
   
    class Meta:
        model = Comment
        fields = ['content' ]
        
    def __init__(self , *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'content',
            FormActions(
                Submit('save', u'发布'),
            )
        )
        
    

