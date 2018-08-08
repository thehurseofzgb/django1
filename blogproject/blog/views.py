from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
import markdown

# Create your views here.

from django.http import HttpResponse
from .models import Article,Categoy

def index(request):
    post_list = Article.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html', context={'post_list':post_list})


def detail(request,pk):
    #get_object_or_404的作用是当传入的 pk 对应的 Article 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在
    post = get_object_or_404(Article, pk= pk)
    post.body = markdown.markdown(post.body,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    num = len(comment_list)
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'num':num
               }
    return render(request,'blog/detail.html',context=context)

#归档视图
def archives(request, year, month):
    post_list = Article.objects.filter(created_time__year = year,created_time__month = month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def category(request, pk):
    cate = get_object_or_404(Categoy, pk=pk)
    post_list = Article.objects.filter(categry= cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})



