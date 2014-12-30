#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf.urls import patterns, include, url
from accounts import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'privatemanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^sendmail/$', views.sendmail , name='sendmail'),
    
    url(r'^login/$', views.login , name='login'),
    url(r'^ssologin/$', views.ssologin , name='ssologin'),
    url(r'^logout/$', views.logout , name='logout'),
    url(r'^register/$', views.register , name='register'),
    url(r'^changepwd/$', views.password_change , name='password_change'),
    url(r'^getpwd/$', views.getpwd , name='getpwd'),
    url(r'^get_active_code/$', views.get_active_code , name='get_active_code'),
   
    
)
