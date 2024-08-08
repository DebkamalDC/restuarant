from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models import *

# Create your views here.
def test(request):
    return HttpResponse('Hello!')

def test1(request):
    return HttpResponse('hiiiiiiiii!!!')

def test2(request):
    return HttpResponse('how r u?')

def test3(request):
    return HttpResponse('abhay & ronit')

def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, "add.html")

def addcode(request):
    a = int(request.GET['num1'])
    b= int(request.GET['num2'])
    c = a+b
    return render(request, 'add.html', {'x':c})

def check(request):
    return render(request, 'check.html')

def checkcode(request):
    a=int(request.GET['ch'])
    o= 'odd'
    e= 'even'
    if (a%2==0):
        return HttpResponse(e)
    else:
        return HttpResponse(o)
    
def login(request):
    return render(request,'login.html')   

def log(request):
    u=man()
    u.username=request.GET['a1']
    u.password=request.GET['a2']
    u.save()
    return render(request,'login.html')

def show(request):
    a=man.objects.all()
    return render(request,'show.html',{'x':a})

def dele(request,id):
    d=man.objects.get(id=id)
    d.delete()
    return redirect("../show")