from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firstapp(request):
    return HttpResponse("Hi from first view")

def firstapp2(request):
    return HttpResponse("<h1>Hi from first view</h2>")

def firstapp3(request):
    a='<h1> yes it is second </h2>'
    return HttpResponse(a)