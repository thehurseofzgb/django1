
from django.contrib import admin
from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    #re_path('^$',views.index,name = 'index'),
    #类视图
    re_path('^$',views.Indexview.as_view(),name = 'index'),
    #re_path('^post/(?P<pk>[0-9]+)/$',views.detail,name = 'detail'),
    re_path('^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name = 'detail'),
    #re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.Archivesviews.as_view(),name='archives'),
    #re_path('^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    re_path('^category/(?P<pk>[0-9]+)/$', views.Categoryview.as_view(), name='category'),
    re_path('^tag/(?P<pk>[0-9]+)/$', views.Tagsviews.as_view(), name='tag'),
    #re_path('^search/$',views.search,name = 'search'),





]
