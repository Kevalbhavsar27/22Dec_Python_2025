from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import *

class Role(models.Model):
    name = models.CharField(max_length=20)

class CustomeUser(AbstractUser):
    username=None
    phone = models.CharField(max_length=20,unique=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)

    USERNAME_FIELD = 'phone'

    objects=CustomUserManager()