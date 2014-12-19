#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf.urls import patterns, url
from mytask import views


urlpatterns = patterns('',
    
    # task 
    url(r'^index/$', views.index , name='index'),
    url(r'^tasks/query/type/(?P<type_id>\S+)/$', views.query_by_type , name='query_by_type'),
    url(r'^tasks/query/level/(?P<level>\S+)/$', views.query_by_level , name='query_by_level'),
    url(r'^tasks/query/pubdate/year/(?P<year>\d+)/$', views.query_by_year , name='query_by_year'),
    url(r'^tasks/query/pubdate/month/(?P<month>\d+)/$', views.query_by_month , name='query_by_month'),
    url(r'^tasks/query/pubdate/day/(?P<day>\d+)/$', views.query_by_day , name='query_by_day'),
    url(r'^tasks/query/isfix/(?P<is_fix>\S+)/$', views.query_by_isfix , name='query_by_isfix'),
    url(r'^add/$', views.add , name='add'),
    url(r'^tasks/(?P<task_id>\d+)/update/$', views.update , name='update'),
    url(r'^tasks/(?P<task_id>\d+)/detail/$', views.detail , name='detail'),
    
    # comment 
    url(r'^tasks/(?P<task_id>\d+)/comments/(?P<c_id>\d+)/delete/$', views.delComment , name='delComment'),
)
