import io
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .Serialzer import StudentSerializer
# Create your views here.
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Student_create(request):
    if request.method== 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)

        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created'}
            json_rdata=JSONRenderer().render(res)
            return HttpResponse(json_rdata,content_type='application/json')

    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
