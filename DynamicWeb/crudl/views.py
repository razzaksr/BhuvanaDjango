from django.shortcuts import redirect, render
from django.http import request

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