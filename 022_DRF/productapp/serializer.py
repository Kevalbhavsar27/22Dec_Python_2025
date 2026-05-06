from rest_framework import serializers
from productapp.models import *


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ProductSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields='__all__'
       
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category'] = CategorySerilizer(instance.category).data
        return resp

