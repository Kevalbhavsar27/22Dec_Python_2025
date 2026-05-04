from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView

# Create your views here.
class ProductView(APIView):

    def get(self,request):
        return Response("GET Calling")
    
    def post(self,request):
        return Response("POST Calling")
    
class ProductViewRetrive(APIView):
    
    def put(self,request,id):
        return Response("PUt calling")
    
    def delete(self,request,id):
        return Response("DELETE Calling")