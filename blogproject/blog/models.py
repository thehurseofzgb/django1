from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User

class Categoy(models.Model):
    #分类数据表
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    #标签表
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    excerpt = models.CharField(max_length=200,blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    categry = models.ForeignKey(Categoy,on_delete=models.CASCADE) #一对多关系，一个分类可以对应多个文章
    tag = models.ManyToManyField(Tag,blank=True)#多对多关系，一个标签可以对应多个文章，一个文章可以有多个标签
    author = models.ForeignKey(User,on_delete=models.CASCADE)#文章作者
    def __str__(self):
        return self.title
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    #这个函数的大概目的是为每个Acticle生成自己的url

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

