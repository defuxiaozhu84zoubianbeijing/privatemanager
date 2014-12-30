#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render 
from django.http import HttpResponse
from privatemanager import settings
import jwt


# Create your views here.
def base(request):
    print 'base'
    return render(request, 'common/base.html' , locals())

# 设置username
def init_username(request):
    # 添加jwt
    duoshuo_jwt_token = None
    if request.user.is_authenticated():
        token = {
            'user_key' : request.user.id ,
            'short_name': settings.DUOSHUO_SHORT_NAME,
            'name' :request.user.username,
            'email' : request.user.email
        }
        duoshuo_jwt_token = jwt.encode(token, settings.DUOSHUO_SECRET)
    # 初始化username
    username = None 
    if 'username'  in request.session :
        username = request.session.get('username')
    if username  is None :
        username = request.user.__unicode__()
    response = HttpResponse(username)
    response.set_cookie('duoshuo_token', duoshuo_jwt_token)
    return response
