from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    students = Student.objects.all()
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        image = request.FILES.get("file")

        Student.objects.create(name=name,email=email,phone=phone,image=image)
        return render(request,"index.html",{"students":students,"msg":"Registration successfully !!!"})


    
    return render(request,"index.html",{"students":students})


def delete(request):
    did = request.GET.get("did")
    student = Student.objects.get(pk=did)
    student.delete()
    return redirect("index")

def update(request):

    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        student = Student.objects.get(pk=id)
        student.name = name
        student.email = email
        student.phone = phone
        student.save()

        return redirect("index")

    students = Student.objects.all()
    uid = request.GET['uid']
    student = Student.objects.get(pk=uid)

    return render(request,"index.html",{"students":students,"student":student})