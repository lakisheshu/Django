from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return  HttpResponse("<h1>hello world </h1>") #for the static data  dispaly
    #render is used merge the static structure and dynamic data
    return render(request,'home.html',{'name':"shehsu"})

def add(request):
    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])

    res= val1+val2

    return render(request,'results.html',{'result':res})