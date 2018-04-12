from django.urls import path,re_path

from myapp import views
urlpatterns=[

   re_path('^students/$',views.students),
   re_path('^attribles/$',views.attribles),
   re_path('^get1$',views.get1),
   #re_path('^get2$',views.get2),
   re_path('^showregist/$',views.showregist),
   re_path('^showregist/regist/$',views.regist),
   re_path('^cookielist/$',views.cookietest),
   re_path('^redirect1/$',views.redirect1),
   re_path('^redirect2/$',views.redirect2),
   re_path('^main/$',views.main),
   re_path('^login/$',views.login),
   re_path('^showmain/$',views.showmain),
]
