from django.shortcuts import render

# Create your views here.

def DTL(request):
    name="Manish"
    place="Jalaun"
    s_name="Gupta"
    marks=90

    my_details={'nm':name,'pla':place,'snm':s_name,'mks':marks}
    return  render(request,'DTL/mydtl.html',my_details)
