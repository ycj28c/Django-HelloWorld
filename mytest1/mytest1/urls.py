#coding=utf-8    
from django.conf.urls import patterns, include, url  
from django.contrib import admin  
import views  

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytest1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='home'),#默认直接进入views的index方法  
)
