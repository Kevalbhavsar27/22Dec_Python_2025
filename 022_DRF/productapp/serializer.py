from rest_framework import serializers
from productapp.models import *


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['address'] = AddressSerializer(instance.address).data    
        return resp

    

class ProductSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields='__all__'
       
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category'] = CategorySerilizer(instance.category).data
        resp['company'] = CompanySerializer(instance.company).data
        return resp

