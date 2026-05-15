from rest_framework import serializers
from myapp.models import *


class RoleSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CustomeUser
        fields='__all__'

    def create(self, validated_data):
        user = CustomeUser.objects.create_user(
            **validated_data
        )
        return user



