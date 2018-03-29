from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def hello1(request):
    return HttpResponse('Hello World1')
def index(request):
    return render(request,'1.html')
