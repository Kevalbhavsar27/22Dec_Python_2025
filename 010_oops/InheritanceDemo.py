class A:
    a = 10
    def display(self):
        print("Display")

#simple or single inheritance
class B(A):
    b = 20
    def show(self):
        print(self.b)
        print(self.a)
#multi level
# class C(B):
#     pass

#Hierarchical
# class C(A):
#     pass

#multiple
# class C(B,A):
#     pass


# b = B()
# b.show()

#***********************************

class Animal:

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def display(self):
        print(self.name,self.type)

class Dog(Animal):
    def __init__(self, name, type,breed):
        super().__init__(name, type)
        self.breed = breed
    
    def display(self):
        print(self.breed)
        super().display()

class Cat(Animal):
    pass


d = Dog("Tommy","Street","German")
d.display()

d1 = Dog("Tigar","pet","Lebrado")
d1.display()

