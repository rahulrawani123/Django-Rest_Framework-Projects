from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serialize=StudentSerializer(stu)
            json_data=JSONRenderer().render(serialize.data)
            return HttpResponse(json_data,content_type="application/json")
        else:
            stu=Student.objects.all()
            serialize=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serialize.data)
            return HttpResponse(json_data,content_type="application/json")
    
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serialize=StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            res={'res':'data created succesfully '}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        return HttpResponse(JSONRenderer().render(serialize.errors))
                
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu,data=python_data)
            if serializer.is_valid():
                serializer.save()
                res={"msg":"Data is updated Succesfully"}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')        
            res={"msg":"data is not valid "}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        res={"msg":"id is not in data "}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            try:
                stu=Student.objects.get(id=id)
            except Student.DoesNotExist:
                res={"msg":"Student with this id does not exist"}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            stu.delete()
            res={"msg":"Data is successfully deleted "}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
            
                
            