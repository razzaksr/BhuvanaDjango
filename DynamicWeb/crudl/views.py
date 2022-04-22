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

def out(request):
    if request.session.has_key('person'):
        request.session['person']=""
        del request.session['person']
    return render(request,'login.html')

def auth(request):
    if request.method=="POST":
        use=request.POST['user']
        pss=request.POST['pass']
        print(use,pss)
        if use=="bhuvana" and pss=="djangorest":
            print("successful")
            request.session['person']=use
            return render(request,'home.html',{"person":request.session['person']})
        else:
            return render(request,'login.html',{"info":"login failed"})
    else:
        return render(request,'login.html',{"info":"login here"})

def hai(request,key=0):#new/update
    
    if request.session.has_key('person'):
        #post section
        if request.method=="POST":
            if key!=0: #update changes ia POST
                print("Updating")
                each=models.Corporates.objects.get(id=key)
                obj=forms.CorporatesForm(request.POST,instance=each)
                
            else: #new addition to corporates
                obj=forms.CorporatesForm(request.POST)
                print(request.POST['org'],"",request.POST['place'])
            if obj.is_valid():
                obj.save()# insertion/ update
                #obj=forms.CorporatesForm()
                #return render(request,'fill.html',{"submission":obj,"data":"Corporate inserted"})
                return redirect("/crudl/home")
        #get section
        else:
            if key!=0: #get corporate to edit
                each=models.Corporates.objects.get(id=key)
                obj=forms.CorporatesForm(instance=each)
            else: # show empty form to add new one
                obj=forms.CorporatesForm()
            return render(request,'fill.html',{"submission":obj,"person":request.session['person']})
    else:
        return render(request,'login.html',{"info":"login here"})

def showing(request):
    if request.session.has_key('person'):
        house=models.Corporates.objects.all();   
        #house=models.Corporates.objects.all().order_by('basic'); 
        return render(request,'list.html',{"mylist":house,"person":request.session['person']})
    else:
        return render(request,'login.html',{"info":"login here"})

def reading(request,unique):
    if request.session.has_key('person'):
        each=models.Corporates.objects.get(id=unique)
        return render(request,'read.html',{"one":each,"person":request.session['person']})
    else:
        return render(request,'login.html',{"info":"login here"})

def editing(request,key):
    if request.session.has_key('person'):
        each=models.Corporates.objects.get(id=key)
        forming=forms.CorporatesForm(request.POST,instance=each)
        #print(forming.org)
        return render(request,'fill.html',{"submission":forming,"person":request.session['person']})
    else:
        return render(request,'login.html',{"info":"login here"})

def remove(request,pos):
    if request.session.has_key('person'):
        each=models.Corporates.objects.get(id=pos)
        models.Corporates.delete(each)
        return redirect("/crudl/home")
    else:
        return render(request,'login.html',{"info":"login here"})

def short(request):
    if request.session.has_key('person'):
        return render(request,'shortlist.html',{"person":request.session['person']})
    else:
        return render(request,'login.html',{"info":"login here"})

def handleShort(request):
    if request.session.has_key('person'):
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
        return render(request,'list.html',{"mylist":handle,"person":request.session['person']})
    else:
        return render(request,'login.html',{"info":"login here"})

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
    single=models.Corporates.objects.get(org=data)
    content=CorpSeri(single)
    return Response(content.data,status=200)

@api_view(['delete'])
def removing(request,key):
    single=models.Corporates.objects.get(id=key)
    models.Corporates.delete(single)
    return Response({"Deleted"})

@api_view(['delete'])
def removingByObject(request):
    single=models.Corporates.objects.get(id=request.data['id'])
    #obj=CorpSeri(instance=request.data)
    #ob=CorpSeri(instance=request.data,data=request.data)
    models.Corporates.delete(single)
    
    
    
    #models.Corporates.delete()
    return Response({"DeletedByObject"})

@api_view(['POST'])
def upCorp(request,id):
    single=models.Corporates.objects.get(id=id)
    got=CorpSeri(instance=single,data=request.data)
    if got.is_valid():
        got.save()
        return Response(got.data)