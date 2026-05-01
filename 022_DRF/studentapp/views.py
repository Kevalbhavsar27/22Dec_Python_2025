from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from studentapp.models import *
from studentapp.serializer import *

@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    ser =  StudentSerilizer(students,many=True)
    return Response({"data":ser.data})


@api_view(['POST'])
def post_student(request):
    ser = StudentSerilizer(data = request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data inserted succssfully !!!"})
   