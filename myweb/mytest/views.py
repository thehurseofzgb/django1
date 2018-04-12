from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Grades,Students
def index(request):
    return HttpResponse('Hello World')
def detail(request,num,num2):
    return HttpResponse('detail-%s-%s'%(num,num2))
def grades(request):
    #模板里取出数据
    gradeslist=Grades.objects.all()
    return render(request,'grades.html',{'grades':gradeslist})
def students(request):
    studentslist=Students.objects.all()
    return  render(request,'students.html',{'students':studentslist})
def gradesStudents(request,num):
    #获得对应班级对象
    grade=Grades.objects.get(pk=num)
    studentslist=grade.students_set.all()
    return  render(request,'students.html',{'students':studentslist})
