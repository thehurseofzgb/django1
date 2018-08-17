#编写自定义模板标签代码,用于处理博客页边栏
from ..models import Article,Categoy,Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag  #装饰器注册模板标签
def get_recent_posts(num = 5):
    return Article.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Article.objects.dates('created_time','month',order = 'DESC')
    #这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义

@register.simple_tag
def get_categories():
    return Categoy.objects.all()

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts = Count('article')).filter(num_posts__gt = 0)


#统计个分类下的文章数

@register.simple_tag()
def get_categories():
    #注意这里的模型名字一定为小写,gt为大于的意思，即过滤出分类数大于0的分类
    return Categoy.objects.annotate(num_posts = Count('article')).filter(num_posts__gt =0)

