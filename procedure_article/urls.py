#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url
from procedure_article import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'privatemanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^init_search/$', views.init_search , name='init_search'),

    url(r'^hello/$', views.hello , name='hello'),
    
    url(r'^init/$', views.init , name='init'),
    url(r'^add/$', views.add , name='add'),

    url(r'^articles/(?P<article_id>\d+)/update/$', views.update , name='update'),
    url(r'^articles/(?P<article_id>\d+)/detail/$', views.detail , name='detail'),
    
    url(r'^articles/query/$', views.search , name='search'),
    url(r'^articles/query/type/(?P<type_id>\d+)/$', views.query_by_type , name='query_by_type'),
    url(r'^articles/query/keyword/(?P<keyword>\S+)/$', views.query_by_keyword , name='query_by_keyword'),
    url(r'^articles/query/author/(?P<author>\S+)/$', views.query_by_author , name='query_by_author'),
    
    url(r'^tongji/(?P<params>\S+)/$', views.tongji , name='tongji'),
    
)
