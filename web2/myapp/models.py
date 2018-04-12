from django.db import models

# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateField()
    ggirlnum=models.IntegerField()
    gboynum=models.IntegerField()
    isdelete=models.BooleanField(default=False)
    def __str__(self):
        return  self.gname
    class Meta:
        db_table='grades'  #定义数据库中数据表名
        ordering=['id']        #定义排序字段

class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(sisdelete=False)#定义一个新管理器的类，重写方法,增加过滤条件

class Students(models.Model):
    #定义自定义模型管理器
    #当自定义以后，objects不存在了
    stuobj=models.Manager()
    stuobj2=StudentsManager()
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField()
    scontend=models.CharField(max_length=20)
    sisdelete=models.BooleanField(default=False)
    #关联外键
    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE,)
    def __str__(self):
        return  self.sname
    class Meta:
        db_table='students'
        ordering=['id']
