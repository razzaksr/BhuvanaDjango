from django.shortcuts import render
from django.http import request
from . import forms

# Create your views here.

def hai(request):
    obj=forms.CorporatesForm()
    return render(request,'fill.html',{"submission":obj})