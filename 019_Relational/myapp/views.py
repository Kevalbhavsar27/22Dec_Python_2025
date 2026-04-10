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
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")

        catObj = Category.objects.get(id=category)
        Product.objects.create(category=catObj,name=name,price=price,qty=qty)

    return redirect("index")