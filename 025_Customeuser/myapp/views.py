from django.shortcuts import render
from myapp.serializer import *
from myapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView, permission_classes
from myapp.permissions import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['POST'])
def create(request):
   ser = UserSerilizer(data=request.data)
   if ser.is_valid():
      ser.save()
      return Response({"data":ser.data})
   else:
      return Response({"errors":ser.errors})
   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_student(request):
   return Response({"message":"stduent created"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_faculty(request):
   return Response({"message":"faculty created"})