from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firsttemp(request):
    return render(request,'first.html')
