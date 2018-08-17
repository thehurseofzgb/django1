from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView
# Create your views here.

from django.http import HttpResponse
from .models import Article,Categoy,Tag

def index(request):
    post_list = Article.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html', context={'post_list':post_list})


def detail(request,pk):
    #get_object_or_404的作用是当传入的 pk 对应的 Article 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在
    post = get_object_or_404(Article, pk= pk)
    post.increase_views()
    # post.body = markdown.markdown(post.body,extensions=[
    #                                  'markdown.extensions.extra',
    #                                  'markdown.extensions.codehilite',
    #                                  'markdown.extensions.toc',
    #                               ])
    #以下方法为自动生成文章目录并且把文章目录增加到post属性中以便在想要的地方显示
    md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    post.body = md.convert(post.body)
    post.toc = md.toc
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


#基于类的通用视图，下列方法将使用类视图代替函数视图
class Indexview(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 1
    #完善分页效果
    def get_context_data(self,**kwargs):
        """
        复写该方法，返回需要的分页对象
        """
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context
    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        # 当前页面左边的页码号
        left =[]
        right =[]
        # 标示第 1 页页码后是否需要显示省略号
        left_has_more = False
        # 标示最后一页页码前是否需要显示省略号
        right_has_more = False
        # 标示是否需要显示第 1 页的页码号。
        # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
        # 其它情况下第一页的页码是始终需要显示的。
        # 初始值为 False
        first = False
        last = False
        page_number = page.number
        # 获得分页后的总页数
        total_pages = paginator.num_pages
        # 获得整个分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
        page_range = paginator.page_range
        if page_number==1:
            # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
            # 此时只要获取当前页右边的连续页码号，
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
            # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。

            right = page_range[page_number:page_number + 2]

            # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
            # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示
            if right[-1]<total_pages-1:
                right_has_more=True
            # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
            # 所以需要显示最后一页的页码号，通过 last 来指示
            if right[-1]<total_pages:
                last =True
        elif page_number ==total_pages:
            # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
            # 此时只要获取当前页左边的连续页码号。
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
            # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] >2:
                left_has_more = True
            if left[1] >1:
                first =True
        else:
            # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
            # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            # 是否需要显示最后一页和最后一页前的省略号
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            # 是否需要显示第 1 页和第 1 页后的省略号
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }
        return data


class Categoryview(Indexview):
    def get_queryset(self):
        cate = get_object_or_404(Categoy, pk=self.kwargs.get('pk'))
        return super(Categoryview, self).get_queryset().filter(categry=cate).order_by('-created_time')

class Archivesviews(Indexview):
    def get_queryset(self):

        return super(Archivesviews, self).get_queryset().filter(created_time__year = self.kwargs.get('year'),created_time__month = self.kwargs.get('month')).order_by('-created_time')

class Tagsviews(Indexview):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk = self.kwargs.get('pk'))
        return super(Tagsviews,self).get_queryset().filter(tag =tag)

from django.views.generic import DetailView
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
# 记得在顶部导入 DetailView
class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify = slugify),
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

#简单搜索
#导入Q的目的是为了能在过滤中直接使用|和&
from django.db.models import Q
def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键字'
        return render(request,'blog/index.html',{'error_msg':error_msg})
    post_list = Article.objects.filter(Q(title__icontains = q)|Q(body__icontains = q))
    return render(request,'blog/index.html',{'error_msg':error_msg,'post_list':post_list})




