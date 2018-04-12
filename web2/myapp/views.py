from django.shortcuts import render
from .models import Students
from django.http import HttpResponse
# Create your views here.
def students(request):
    studentslist=Students.stuobj2.all()
    return  render(request,'students.html',{'students':studentslist})
def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    return  HttpResponse('zgb')

#获取GET传递的数据,获取同名的多个参数需要用getlist方法

def get1(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    c=request.GET.get('c')
    return HttpResponse(a+b+c)
def showregist(request):
    return  render(request,'regist.html')


def regist(request):
    name=request.POST.get('name')#键名为模板中的
    gender=request.POST.get('gender')
    age=request.POST.get('age')
    hobby=request.POST.getlist('hobby')
    print(name)
    return HttpResponse('post')
#cookie
def cookietest(request):
    res=HttpResponse()
    cookie=request.COOKIES            #获取cookie
    res.write("<h1>"+cookie['zgb']+"</h1>")
    #cookie=res.set_cookie("zgb","good")   #设置cookie
    return  res



#重定向视图

from  django.http import HttpResponseRedirect
from  django.shortcuts import redirect
def redirect1(request):
    return HttpResponse('zgb is good')

def redirect2(request):
    return HttpResponseRedirect('/zgb/redirect1')#绝对路径
    #return redirect('/zgb/redirect1')


#session
def main(request):
    return render(request,"main.html")

def login(request):
    return  render(request,"login.html")

def showmain(request):
    return redirect('/zgb/main')







