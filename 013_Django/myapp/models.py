from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
