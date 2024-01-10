from django.shortcuts import render,redirect
from mongoengine import *
from django.http import request,HttpResponse
from . import documents
from certifi import *
# Create your views here.

# myCert=where()
dbConnect=connect(host='mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority',db='yogesh')

def showDelete(request,id):
    one = documents.resources.objects(resource_id=id).first()
    documents.resources.delete(one)
    return redirect('/erp/list')

def showReadOne(request,id):
    if request.method=="GET":
        one = documents.resources.objects(resource_id=id).first()
        return render(request,'modify.html',{"data":one})
    else:
        resource_id=int(request.POST['resource_id'])
        resource_name=request.POST['resource_name']
        resource_skills=request.POST['resource_skills'].split(",")
        resource_contact=int(request.POST['resource_contact'])
        resource_experience=int(request.POST['resource_experience'])
        documents.resources.objects(resource_id=resource_id).update_one(set__resource_name=resource_name,
                                                                        set__resource_skills=resource_skills,
                                                                        set__resource_contact=resource_contact,
                                                                        set__resource_experience=resource_experience)
        return redirect("/erp/list")
        

def showNew(request):
    if request.method=="GET":
        return render(request,'join.html')
    else:
        expert = documents.resources()
        expert.resource_name=request.POST['resource_name']
        expert.resource_skills=request.POST['resource_skills'].split(",")
        expert.resource_contact=int(request.POST['resource_contact'])
        expert.resource_experience=int(request.POST['resource_experience'])
        expert.save()
        print(expert)
        return redirect('/erp/list')

def showHome(request):
    return render(request,'home.html')

def check(request):
    data=documents.resources.objects.all()
    return render(request,'listall.html',{"records":data})
