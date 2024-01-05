from django.http import HttpResponse, request,response
from django.shortcuts import render



# Create your views here.

def haiThere(request):
    return HttpResponse("<h1>Zealous Tech Corp</h1>")

def tempAccess(request):
    return render(request,'hell.html')

def gotInput(request,mynum):
    return render(request,'hell.html',{'data':mynum*2})

def showImg(request):
    return render(request,'myresource.html')