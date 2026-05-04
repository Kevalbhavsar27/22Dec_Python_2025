from rest_framework import serializers
from studentapp.models import *

class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        # fields = ['id','name']
        # exclude = ['age']