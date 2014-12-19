import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib import admin
from mytask.models import Task , Comment , Type

# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Type)
