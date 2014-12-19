#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'privatemanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^common/', include('common.urls')),
    url(r'^procedure_article/', include('procedure_article.urls')),
    url(r'^mytask/', include('mytask.urls')),
    
)
