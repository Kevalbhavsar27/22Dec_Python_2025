from faker import Faker
import random
fk = Faker()
from myapp.models import *

def create(n=50):
    for i in range(n):
        name = fk.name()
        email = fk.email()
        age = random.randint(20,25)
        stid = f"ST_{random.randint(100,999)}"
        stid_obj = StudentId.objects.create(stid=stid)
        Student.objects.create(name=name,email=email,age=age,stid=stid_obj)
    print("done")


def marks():
    studetns = Student.objects.all()
    for st in studetns:
        sub = Subjects.objects.all()
        for s in sub:
            Marks.objects.create(student=st,subject=s,marks=random.randint(1,50))
