from django.shortcuts import redirect, render
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CorpSeri

from . import models
from . import forms

# Create your views here.

house=[]

def hai(request,key=0):#new/update
    #post section
    if request.method=="POST":
        if key!=0: #update changes ia POST
            each=models.Corporates.objects.get(id=key)
            obj=forms.CorporatesForm(request.POST,instance=each)
        else: #new addition to corporates
            obj=forms.CorporatesForm(request.POST)
        if obj.is_valid():
            obj.save()# insertion/ update
            #obj=forms.CorporatesForm()
            #return render(request,'fill.html',{"submission":obj,"data":"Corporate inserted"})
            return redirect("/crudl/")
    #get section
    else:
        if key!=0: #get corporate to edit
            each=models.Corporates.objects.get(id=key)
            obj=forms.CorporatesForm(instance=each)
        else: # show empty form to add new one
            obj=forms.CorporatesForm()
        return render(request,'fill.html',{"submission":obj})

def showing(request):
    house=models.Corporates.objects.all();   
    #house=models.Corporates.objects.all().order_by('basic'); 
    return render(request,'list.html',{"mylist":house})

def reading(request,unique):
    each=models.Corporates.objects.get(id=unique)
    return render(request,'read.html',{"one":each})

def editing(request,key):
    each=models.Corporates.objects.get(id=key)
    forming=forms.CorporatesForm(request.POST,instance=each)
    #print(forming.org)
    return render(request,'fill.html',{"submission":forming})

def remove(request,pos):
    each=models.Corporates.objects.get(id=pos)
    models.Corporates.delete(each)
    return redirect("/crudl/")

def short(request):
    return render(request,'shortlist.html')

def handleShort(request):
    try:
        nat=request.POST['nature']
    except KeyError as k:
        nat=""
    try:
        open=request.POST['skills']
    except KeyError as ky:
        open=""
    try:
        rat=request.POST['rate']
    except KeyError as ke:
        rat=""
    try:
        sal=request.POST['salary']
    except KeyError as ke:
        sal=""
    
    print(nat,open,sal,rat)
    
    if nat!="" and open=="" and sal=="" and rat=="":
        handle=models.Corporates.objects.filter(nature__exact=nat)
    elif nat=="" and open!="" and sal=="" and rat=="":
        handle=models.Corporates.objects.filter(opennings__icontains=open)
    elif nat=="" and open=="" and sal!="" and rat=="":
        handle=models.Corporates.objects.filter(basic__gte=sal)
    elif nat=="" and open=="" and sal=="" and rat!="":
        handle=models.Corporates.objects.filter(ratings__lte=rat)
    return render(request,'list.html',{"mylist":handle})

@api_view(['POST'])
def newCorp(request):
    got=CorpSeri(data=request.data)
    
    if got.is_valid():
        got.save()
        return Response(got.data)

@api_view(['GET'])
def listAll(request):
    every=models.Corporates.objects.all()
    content=CorpSeri(every,many=True)
    return Response(content.data,status=200)

@api_view(['GET'])
def individual(request,data):
    single=models.Corporates.objects.get(id=data)
    content=CorpSeri(single)
    return Response(content.data,status=200)

@api_view(['delete'])
def removing(request,key):
    single=models.Corporates.objects.get(id=key)
    models.Corporates.delete(single)
    return Response({"Deleted"})