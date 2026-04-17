
from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):

    
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,"index.html",{"categories":categories,"products":products})

def add_product(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        catObj = Category.objects.get(id=category)
        if id :
            product = Product.objects.get(pk=id)
            product.category = catObj
            product.name = name
            product.price=price
            product.qty=qty
            product.save()
            
        else:
            Product.objects.create(category=catObj,name=name,price=price,qty=qty)
           

    return redirect("index")


def delete_product(request):
    id = request.GET['id']
    p = Product.objects.get(pk=id)
    p.delete()
    return redirect("index")

def update_product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    id = request.GET['id']
    p = Product.objects.get(pk=id)


   
    return render(request,"index.html",{"product":p,"categories":categories,"products":products})