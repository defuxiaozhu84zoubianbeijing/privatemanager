
from django.conf.urls import patterns, url
from common import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'douban.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),
        
    url(r'^$', views.base, name='base'),
    url(r'^init_username/$', views.init_username, name='init_username'),
    
)
