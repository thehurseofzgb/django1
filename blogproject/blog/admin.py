from django.contrib import admin
from django.contrib import admin
from .models import Article, Categoy, Tag

class postadmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','categry','author']
#注册
admin.site.register(Article,postadmin)
admin.site.register(Categoy)
admin.site.register(Tag)
# Register your models here.
