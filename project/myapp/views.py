from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework import viewsets, status
def index(request):
    return  Response("done")


class CategoryViewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer