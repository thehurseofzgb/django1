
from django.contrib import admin
from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path('^$',views.index,name = 'index'),
    re_path('^post/(?P<pk>[0-9]+)/$',views.detail,name = 'detail'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    re_path('^category/(?P<pk>[0-9]+)/$', views.category, name='category'),



]
