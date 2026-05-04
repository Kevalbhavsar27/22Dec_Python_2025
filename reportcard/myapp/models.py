from django.db import models


# Create your models here.
class StudentId(models.Model):
    stid = models.CharField(max_length=20)

    def __str__(self):
        return self.stid

class Student(models.Model):
    stid = models.OneToOneField(StudentId,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

class Subjects(models.Model):
    name = models.CharField(max_length=20)

class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    marks = models.FloatField()