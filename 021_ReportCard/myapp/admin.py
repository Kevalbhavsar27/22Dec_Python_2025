from django.contrib import admin
from myapp.models import *
# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display =["stid","name","email","age"]

admin.site.register(StudentId)
admin.site.register(Student,StudentDisplay)
admin.site.register(Subjects)
admin.site.register(Marks)