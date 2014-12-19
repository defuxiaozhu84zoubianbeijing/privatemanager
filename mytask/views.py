#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from mytask.models import Type , Task , Comment
from mytask.forms import TaskForm, CommentForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

# 查询
def _query(request , params=None):
    type_set = Type.objects.filter(state=True)
    if params is None :
        tasks = Task.objects.filter(state=True).filter(publisher=request.user)
    else :
        if params[0] == 'level':
            tasks = Task.objects.filter(state=True).filter(publisher=request.user).filter(level=params[1])
        elif params[0] == 'type' :
            tasks = Task.objects.filter(state=True).filter(publisher=request.user).filter(type=params[1])
        elif params[0] == 'year':
            tasks = Task.objects.filter(state=True).filter(publisher=request.user).filter(pubdate__year=params[1])
        elif params[0] == 'month':
            tasks = Task.objects.filter(state=True).filter(publisher=request.user).filter(pubdate__month=params[1])
        elif params[0] == 'day':
            tasks = Task.objects.filter(state=True).filter(publisher=request.user).filter(pubdate__day=params[1])
        elif params[0] == 'is_fixed':
            tasks = Task.objects.filter(state=True).filter(publisher=request.user).filter(is_fixed=params[1])
    return render(request , 'mytask/mytask_index.html' , locals()) 

def _oprate(request , instance=None):
    form = None 
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=instance)
        if form.is_valid():
            task = form.save(commit=False)
            task.publisher = request.user
            task.save()
            return HttpResponseRedirect('/mytask/index/')
        else :
            error_messages = u'操作出错，请检查'
    else :
        form = TaskForm(instance=instance)
    return render(request , 'mytask/mytask_oprate.html' , locals())

# 首页显示全部
@login_required(login_url='/accounts/login/')
def index(request):
    return _query(request , None)

# 根据任务级别查询
def query_by_level(request , level):
    params = ['level' , level]
    return _query(request , params)

# 根据任务类型查询   
def query_by_type(request , type_id):
    _type = get_object_or_404(Type , pk=type_id)
    params = ['type' , _type]
    return _query(request , params)

# 根据年份查询
def query_by_year(request , year):
    params = ['year' , year]
    return _query(request , params)

# 根据月份查询
def query_by_month(request , month):
    params = ['month' , month]
    return _query(request , params)

# 根据日期查询
def query_by_day(request , day):
    params = ['day' , day]
    return _query(request , params)

# 根据项目是否结束查询
def query_by_isfix(request , is_fix):
    is_fixed = False 
    if is_fix == 'True' :
        is_fixed = True   
    params = ['is_fixed' , is_fixed]
    return _query(request , params)

# 添加任务
def add(request):
    return _oprate(request , None)

# 修改任务
def update(request , task_id):
    task = get_object_or_404(Task , pk=task_id)
    return _oprate(request, task) 

# 显示任务详细
def detail(request , task_id):
    type_set = Type.objects.filter(state=True)
    task = get_object_or_404(Task , pk=task_id)
    comments = Comment.objects.filter(state=True).filter(task=task)
    return addComment(request , type_set , comments, task)      

# 添加评论
def addComment(request , type_set , comments , task):
    form = None 
    if request.method == 'POST' :
        if request.user.is_authenticated():
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.publisher = request.user
                comment.task = task
                comment.save()
                return HttpResponseRedirect('/mytask/tasks/' + str(task.id) + '/detail/')
            else :
                error_messages = u'抱歉，暂时无法评论'
        else :
            return HttpResponseRedirect('/accounts/login/')
    else :
        form = CommentForm()
    return render(request , 'mytask/mytask_detail.html' , locals())

# 删除评论
def delComment(request , task_id , c_id):
    comment = get_object_or_404(Comment , pk=c_id)
    comment.delete()
    return HttpResponseRedirect('/mytask/tasks/' + str(task_id) + '/detail/')
    
    




