from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):  
    all = Student.objects.all()
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(name=name,email = email,age=age)

        
        return render(request,"index.html",{"msg":"registration suceess","students":all})  
    return render(request,"index.html",{"students":all})

def delete(request):
    did = request.GET['did']
    st = Student.objects.get(id=did)
    st.delete()
    return redirect("index")
    
