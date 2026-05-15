from django.urls import path
from myapp.views import *

urlpatterns = [

    path("create",create,name="create"),

    path("students",create_student,name="students"),
    path("faculty",create_faculty,name="faculty")
]