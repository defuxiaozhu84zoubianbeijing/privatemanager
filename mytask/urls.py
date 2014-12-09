#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from mytask import views


urlpatterns = patterns('',
    
    # task 
    url(r'^index/$', views.index , name='index'),
    url(r'^tasks/query/type/(?P<level>\S+)/$', views.query_by_level , name='query_by_level'),
    url(r'^tasks/query/level/(?P<type_id>\d+)/$', views.query_by_type , name='query_by_type'),
    url(r'^tasks/query/pubdate/(?P<pub_date>\S+)/$', views.query_by_pubdate , name='query_by_pubdate'),
    url(r'^add/$', views.add , name='add'),
    url(r'^tasks/(?P<task_id>\d+)/update/$', views.update , name='update'),
    url(r'^tasks/(?P<task_id>\d+)/detail/$', views.detail , name='detail'),
    
    # comment 
    url(r'^tasks/(?P<task_id>\d+)/comments/(?P<c_id>\d+)/delete/$', views.delComment , name='delComment'),
)
