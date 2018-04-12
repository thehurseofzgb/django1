from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#注册
class StudentsAdmin_inf(admin.TabularInline):#关联
    model = Students
    extra = 2
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsAdmin_inf]
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isdelete']  #字段排列
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page =5
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):#设置页面的名称,添加字段描述
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'
    def isdelete(self):
        if self.sgender:
            return '是'
        else:
            return '否'
    list_display = ['pk','sname','sage',gender,'scontend','sgrade',isdelete]

admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)
