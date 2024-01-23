from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from mongoengine import *
from django.http import request,HttpResponse
from . import documents
from certifi import *
# Create your views here.

# myCert=where()
dbConnect=connect(host='mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority',db='yogesh')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showLogin(request):
    if request.method=="GET":
        return render(request,'index.html')
    else:
        user=request.POST['username']
        pas=request.POST['password']
        if user == "yokesh" and pas=="zealous":
            request.session['auth']=user
            return redirect('/erp/home')
        else:
            return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showLogout(request):
    if request.session.has_key('auth'):
        del request.session['auth']
    return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showShort(request):
    if request.session.has_key('auth'):
        if request.method=="GET":
                return render(request,'filter.html')
        else:
            skill=request.POST['skill']
            exp=request.POST['exp']
            if skill != "" and exp=="":
                print(skill)
                data = documents.resources.objects(resource_skills__contains=str(skill))
                return render(request,'listall.html',{"records":data})
            elif skill == "" and exp!="":
                exp=int(exp)
                data = documents.resources.objects.filter(resource_experience__gte=exp)
                return render(request,'listall.html',{"records":data})
            else:
                return redirect('/erp/shortlist')
    else:
        return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showDelete(request,id):
    if request.session.has_key('auth'):
        one = documents.resources.objects(resource_id=id).first()
        documents.resources.delete(one)
        return redirect('/erp/list')
    else:
        return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showReadOne(request,id):
    if request.session.has_key('auth'):
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
    else:
        return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showNew(request):
    if request.session.has_key('auth'):
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
    else:
        return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def showHome(request):
    if request.session.has_key('auth'):
        return render(request,'home.html')
    else:
        return redirect('/erp/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def check(request):
    if request.session.has_key('auth'):
        data=documents.resources.objects.all()
        return render(request,'listall.html',{"records":data})
    else:
        return redirect('/erp/')
