from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def first(request):
    return HttpResponse("<h1>Welcome to DJango</h1>")

def second(request):
    return render(request,'myfirst.html')

def third(request):
    return render(request,'mysecond.html',{"mydata":"hello there!","myaddition":34.6})

def fourth(request):
    return render(request,'audvid.html')

def fifth(request,data):
    return render(request,'params.html',{"hey":calculate(data)})

def calculate(data):
    return data*data*data

def showlog(request):
    return render(request,'formsub.html')

def recform(request):
    # print(request.GET['user'])
    # print(request.GET['pass'])
    u=request.POST['user']
    p=request.POST['pass']
    
    if u=="bhuvana" and p=="salem":
        return render(request,'formsub.html',{"data":"authorised user"})
    else:
        return render(request,'formsub.html',{"data":"unauthorised user"})