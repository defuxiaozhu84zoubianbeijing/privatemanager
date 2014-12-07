#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from procedure_article.models import Type , Article , Comment

# Register your models here.
admin.site.register(Type)
admin.site.register(Article)
admin.site.register(Comment)


