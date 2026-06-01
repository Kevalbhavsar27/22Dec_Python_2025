from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from myapp.models import *
from myapp.serializer import *
from rest_framework import viewsets, status
from rest_framework.permissions import *

def index(request):
    return  Response("done")


class CategoryViewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
       
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

class ProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
       
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer