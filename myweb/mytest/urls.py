
from django.urls import path,re_path
from . import views
urlpatterns=[
    path('', views.index),
    re_path('^(\d+)/(\d+)/$',views.detail),     # 正则匹配所有数字
    re_path('^grades/$',views.grades),
    re_path('^students/$',views.students),
    re_path('^grades/(\d+)',views.gradesStudents),
]
