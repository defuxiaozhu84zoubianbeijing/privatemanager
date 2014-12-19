#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from accounts.forms import loginForm, registerForm, PwdHelperForm, \
    PassWordChangeForm
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as user_login 
from django.contrib.auth import logout as user_logout
from django.contrib.auth.models import User
from privatemanager import settings 
from common import const
import logging
import utils 
from accounts.models import PwdHelper, PwdQuestion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# 添加logger
logger = logging.getLogger(__name__) 


# Create your views here.

# 登陆
def login(request):
    form = None 
    if request.method == 'POST' :
        form = loginForm(request.POST)
        try :
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username , password=password)
            if user is not None :
                if user.is_active:
                    user_login(request, user)
                    logger.debug(request.user.__unicode__() + u':登陆成功')
                    return HttpResponseRedirect('/procedure_article/init/')
                else :
                    logger.debug(u'登陆失败:用户还没有注册')
                    error_messages = u'用户还没有注册'
            else :
                logger.debug(request.user.__unicode__() + u':登陆失败:用户名或密码输入错误，请重新输入')
                error_messages = u'用户名或密码输入错误，请重新输入'
        except Exception as er :
            form.is_valid()
            logger.debug(request.user.__unicode__() + u':登录失败'.join(str(er)))
            pass
    else : 
        form = loginForm()
    return render(request , 'accounts/login.html' , locals())

# 注销
def logout(request):
    logger.debug(request.user.__unicode__() + u':注销')
    user_logout(request)
    return HttpResponseRedirect('/procedure_article/init/')

# 注册
def register(request):
    form = None 
    if request.method == 'POST' :
        form = registerForm(request.POST)
        if form.is_valid():
            _username = request.POST.get('username')
            _password = request.POST.get('password')
            _email = request.POST.get('email')
            _question_id = request.POST.get('question')
            _answer = request.POST.get('answer')
            _user = User.objects.create_user(_username , _email , _password)
            # 保存找回密码问题
            try :
                _question = PwdQuestion.objects.get(pk=int(_question_id))
                pwdHelper = PwdHelper(user=_user , question=_question , answer=_answer)
                pwdHelper.save()
            except :
                # 出现异常，删除用户，保证数据准确性
                _user.delete()
            # 提升用户权限
            user = authenticate(username=_username , password=_password)
            if user is not None :
                if user.is_active:
                    logger.debug(request.user.__unicode__() + u':注册成功')
                    user_login(request, user)
                    return HttpResponseRedirect('/accounts/get_active_code/')
                else :
                    logger.debug(request.user.__unicode__() + u':注册失败:用户没有激活，请到邮箱激活！')
                    error_messages = u'用户没有激活，请到邮箱激活！'
            else:
                logger.debug(request.user.__unicode__() + u':注册失败:请重新注册')
                error_messages = u'请重新注册'
        else : 
            error_messages = u'请重新注册'
    else :
        form = registerForm()
    return render(request , 'accounts/register.html' , locals())

# 获取激活码
def get_active_code(request):
    return render(request , 'accounts/getactivecode.html' , locals())

# 发送邮件
def sendmail(request):
    _email = str(request.user.email)
    if _email is not None :
        _dict = None
        _email = utils.check_email(_email)
        options = {
             'subject' : const.ACTIVE_CODE_SUBJECT,
             'from_email' : settings.EMAIL_HOST_USER,
             'text_content' : u'注册成功，欢迎登陆' ,
             'html_content' : u'<h3 align="center">注册私人管家网站,您的激活码是19840905</h3><h4 align="center"><a href="http://127.0.0.1:8000/procedure_article/init/">请点此链接激活</h4>',
             'to_mail' : _email    
        }
        _dict = utils._send_mail(request, options)
        flag = _dict['flag']
        if flag :
            return HttpResponse('True')
        else :
            return HttpResponse('False')
    else :
        logger.debug(request.user.__unicode__() + ':发送邮件失败,用户邮箱为None')  
    return HttpResponse('False')


# 找回密码
def getpwd(request):
    logger.debug(request.user.__unicode__() + ':找回密码启动')
    form = None 
    if request.method == 'POST' :
        form = PwdHelperForm(request.POST)
        if form.is_valid() :
            # 验证答案是否正确
            _answer = request.POST.get('answer')
            _email = request.POST.get('email')
            try :
                _user = User.objects.filter(email=_email)[0]
                if _user is not  None :
                    _pwdHelper = PwdHelper.objects.filter(user=_user)[0]
                    if _answer == _pwdHelper.answer :
                        # 修改密码
                        flag = _pwd_change(request , const.ORIGINAL_PWD , _user)
                        if flag == False :
                            error_messages = u'用户邮箱输入错误，请重试'
                        else:  
                            # 发送邮件
                            option = {
                                 'subject' : const.PWD_GET_SUBJECT,
                                 'from_email' : settings.EMAIL_HOST_USER,
                                 'text_content' : u'找回密码成功' ,
                                 'html_content' : u'<h3 align="center">你的密码是' + const.ORIGINAL_PWD + '</h3><h4 align="center"><a href="http://127.0.0.1:8000/accounts/login/">请点此链接返回网站登录</h4>',
                                 'to_mail' : [_email]   
                            }
                            options = [option]
                            flag = utils.send_multiple_email(options)
                            if flag :
                                logger.debug(request.user.__unicode__() + ',找回密码成功 ')  
                                error_messages = u'找回密码成功，前往邮箱查看新密码。登陆！'
                            else : 
                                logger.debug(request.user.__unicode__() + u',发送邮件失败')  
                                error_messages = u'您输入的邮箱有误，请重新检查'
                    else :
                        logger.debug(request.user.__unicode__() + u',找回密码失败，找回问题回答错误') 
                        error_messages = u'答案错误，请重试'
                else :
                    logger.debug(request.user.__unicode__() + u',找回密码失败，没有找到注册邮箱，请检查输入') 
                    error_messages = u'没有找到注册邮箱，请检查输入'
            except Exception as er : 
                logger.debug(request.user.__unicode__() + u' : 错误原因为' + str(er)) 
                error_messages = str(er) 
    else :
        form = PwdHelperForm()
    return render(request , 'accounts/getpwd.html' , locals()) 

# 重置用木密码
@login_required(login_url='/accounts/login/')
def password_change(request):
    form = None 
    if request.method == 'POST' :
        form = PassWordChangeForm(request.POST,)
        if form.is_valid():
            # 添加一系列验证
            _password = request.POST.get('password')
            flag = _pwd_change(request , _password , request.user)
            if flag :
                return HttpResponseRedirect('/procedure_article/init/')
        else :
            error_messages = u'用户输入错误'
    else :
        form = PassWordChangeForm()
    return render(request , 'accounts/passwordChange.html' , locals())

# 修改密码的原始方法
def _pwd_change(request , new_pwd='' , user=None):
    _new_pwd = make_password(new_pwd , salt=None , hasher='default')
    if user is not None :
        user.password = _new_pwd
        user.save()
        update_session_auth_hash(request, user)
        return True
    else :
        return False 
    





