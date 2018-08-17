from django.db import models
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

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
    #统计文章阅读量
    views = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])
    def __str__(self):
        return self.title
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    #这个函数的大概目的是为每个Acticle生成自己的url

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']


    #生成摘要
    #导入markdown,strip_tags,如果没有写摘要则自动生成以后把markdown文本转化为html文本，注意这里的save方法是复写的方法，如果有摘要，则调用原本的save方法，注意该方法不能动态的显示摘要
    def save(self,*args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:30]
        super(Article,self).save(*args,**kwargs)


