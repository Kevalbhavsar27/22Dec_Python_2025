from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    students = Student.objects.all()
    return JsonResponse({"students":list(students.values())})

def add_user(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(name=name,email=email,age=age)

        return HttpResponse("Registration successfully !!!")
    

def delete_user(request):
    id  = request.GET['id']
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponse("Student deleted !!!")


def edit_user(request):
    id  = request.GET['id']
    student = Student.objects.filter(id=id)
    return JsonResponse({"student":list(student.values())})


def update_user(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        st = Student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        st.save()

        return HttpResponse("Update successfully !!!")
    

def search(request):
    q = request.GET['q']

    # students = Student.objects.filter(name__startswith=q) or Student.objects.filter(email__startswith=q) or Student.objects.filter(age__startswith=q)

    students = Student.objects.filter(Q(name__startswith=q)|Q(email__startswith=q)|Q(age__startswith=q)) 

    return JsonResponse({"students":list(students.values())})