#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from accounts.models import PwdHelper , PwdQuestion , UserProfile
# Register your models here.

# admin.site.register(PwdHelper)
# admin.site.register(PwdQuestion)

admin.site.register(PwdHelper)
admin.site.register(PwdQuestion)
admin.site.register(UserProfile)
