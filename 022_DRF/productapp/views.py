from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from productapp.models import *
from productapp.serializer import *
# Create your views here.
class ProductView(APIView):

    def get(self,request):
        products = Product.objects.all()
        ser = ProductSerilizer(products,many=True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = ProductSerilizer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted successfully"})
        else:
            return Response({"error":ser.errors,"message":"somethong went wrong"})
    
    
class ProductViewRetrive(APIView):
    
    def put(self,request,id):
        return Response("PUt calling")
    
    def delete(self,request,id):
        return Response("DELETE Calling")
    


class CategoryView(APIView):

    def get(self,request):
       categories = Category.objects.all()
       ser = CategorySerilizer(categories,many=True)
       return Response({"data":ser.data})
    
    def post(self,request):
        ser = CategorySerilizer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted successfully"})
        else:
            return Response({"error":ser.errors,"message":"somethong went wrong"})
    
class CategoryViewRetrive(APIView):
    
    def put(self,request,id):
        category = Category.objects.get(pk=id)
        ser = CategorySerilizer(category,request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"Data update successfully"})
        else:
            return Response({"error":ser.errors,"message":"somethong went wrong"})

    
    def delete(self,request,id):
        category = Category.objects.get(pk=id)
        category.delete()
        return Response({"message":"Data deleted"})
    
@api_view(['GET'])
def product_by_category(request,id):
    category = Category.objects.get(pk=id)
    products = Product.objects.filter(category=category)
    ser = ProductSerilizer(products,many=True)
    return Response({"data":ser.data})