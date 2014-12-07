#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from procedure_article.models import Type, Article, Comment
from crispy_forms.bootstrap import  *
from crispy_forms.helper import Layout , FormHelper
from crispy_forms.layout import Submit , Reset


class ArticleForm(ModelForm):
    
    KEY_WORD_CHOICES = (
        ('python', 'python'), ('django', 'django'),
        ('mysql', 'mysql'), ('oracle', 'oracle'),
        ('sqlserver', 'sqlserver'), ('jquery', 'jquery'),
        ('apache', 'apache'), ('bootstrap', 'bootstrap'),
        ('数据结构', '数据结构'), ('SVN', 'SVN'), ('Git', 'Git'),
    )

    # 文章作者
    author = forms.CharField(
        label='作者',
        max_length=30 ,
        required=True ,
        error_messages={'required': '请输入文章作者姓名', 'error':'作者姓名做多可输入30个字符'},
    )
    # 文章类型 
    type = forms.ModelChoiceField(
        label='类型 ',
        empty_label='请选择文章类别' ,
        queryset=Type.objects.filter(state=True).exclude(parentId=0),
        to_field_name='id',
        required=True ,
        error_messages={'required': '请选择文章类型'},
    )
    # 关键字
    keyword = forms.MultipleChoiceField(
        label='关键字',
        choices=KEY_WORD_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        error_messages={'required': '请选择关键字'},
    )  
    # 文章标题
    title = forms.CharField(
        label='标题',
        max_length=200 ,
        required=True ,
        error_messages={'required': '请输入文章标题', 'error':'文章标题做多可输入200个字符'},
    )
    # 文章简介
    jianjie = forms.CharField(
        label='简介',
        max_length=200 ,
        required=True ,
        error_messages={'required': '请添加文章概要', 'error':'文章简介做多可输入200个字符'},
    )
    # 文章内容
    content = forms.Textarea()

    class Meta:
        model = Article
        fields = [ 'author' , 'type', 'keyword' , 'title', 'jianjie' , 'content' ]
        
        
    def __init__(self , *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'author',
            'type' ,
            InlineCheckboxes('keyword'),
            'title' ,
            'jianjie',
            'content',
            FormActions(
                Submit('save', '保存'),
                Reset('reset', '重置'),
            )
        )
        
        
        
class CommentForm(ModelForm):
    content = forms.Textarea()
   
    class Meta:
        model = Comment
        fields = ['content' ]
        
    def __init__(self , *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'cone'
        
        
        
    




