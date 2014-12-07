#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render 
from django.http import HttpResponse


# Create your views here.
def base(request):
    print 'base'
    return render(request, 'common/base.html' , locals())

# 设置username
def init_username(request):
    username = None 
    if 'username'  in request.session :
        username = request.session.get('username')
    if username  is None :
        username = request.user.__unicode__()
    return HttpResponse(username)
