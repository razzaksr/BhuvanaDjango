from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def first(request):
    return HttpResponse("<h1>Welcome to DJango</h1>")

def second(request):
    return render(request,'myfirst.html')

def third(request):
    return render(request,'mysecond.html',{"mydata":"hello there!"})