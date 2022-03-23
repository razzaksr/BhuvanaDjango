from django.shortcuts import render
from django.http import request

from . import models
from . import forms

# Create your views here.

house=[]

def hai(request):
    if request.method=="POST":
        obj=forms.CorporatesForm(request.POST)
        if obj.is_valid():
            obj.save()# insertion
            obj=forms.CorporatesForm()
            return render(request,'fill.html',{"submission":obj,"data":"Corporate inserted"})
        else:
            return render(request,'fill.html',{"submission":obj,"data":"Corporate hasn't inserted"})
    else:
        obj=forms.CorporatesForm()
    return render(request,'fill.html',{"submission":obj})

def showing(request):
    house=models.Corporates.objects.all();
    return render(request,'list.html',{"mylist":house})

def reading(request,unique):
    each=models.Corporates.objects.get(id=unique)
    return render(request,'read.html',{"one":each})