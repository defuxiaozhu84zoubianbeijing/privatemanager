#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from mytask.models import Type , Task , Comment
from mytask.forms import TaskForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# 首页显示全部
@login_required(login_url='/accounts/login/')
def index(request):
    type_set = Type.objects.filter(state=True)
    
    tasks = Task.objects.filter(state=True).filter(publisher=request.user)
    return render(request , 'mytask/mytask_index.html' , locals())

# 查询
def _query(request):
    return None 

def query_by_level(request , level):
    return  None 

def query_by_type(request , type_id):
    return None 

def query_by_pubdate(request , pub_date):
    return None 

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

def add(request):
    return _oprate(request , None)

def update(request , task_id):
    task = get_object_or_404(Task , pk=task_id)
    return _oprate(request, task) 

def detail(request , task_id):
    type_set = Type.objects.filter(state=True)
    task = get_object_or_404(Task , pk=task_id)

    comments = Comment.objects.filter(state=True).filter(task=task)
    
    return addComment(request , type_set , comments, task)      

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

def delComment(request , task_id , c_id):
    comment = get_object_or_404(Comment , pk=c_id)
    comment.delete()
    return HttpResponseRedirect('/mytask/tasks/' + str(task_id) + '/detail/')
    
    




