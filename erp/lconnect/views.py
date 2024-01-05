from django.shortcuts import render
from mongoengine import *
from django.http import request,HttpResponse
from . import documents
from certifi import *
# Create your views here.

# myCert=where()
dbConnect=connect(host='mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority',db='yogesh')

def check(request):
    data=documents.resources.objects.all()
    for d in data:print(d)
    # hai=documents.resources()
    # hai.born("Annamalai S",76567676734,['Java Script','Python'],5)
    # print(hai)
    # hai.save()
    return HttpResponse("<p>okay</p>")
