#编写自定义模板标签代码,用于处理博客页边栏
from ..models import Article,Categoy
from django import template

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
