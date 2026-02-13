class Student:

    collage = "ABC"
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

    def display(self):
        print(self.id,self.name,self.email,self.collage)

    @classmethod
    def test(cls):
        print(cls.collage)

    @staticmethod
    def sample():
        print("sample calling")


Student.collage="XYZ"

s  = Student(10,"Chetan","chetan@gmail.com")
s.display()

s1 = Student(11,"jagdish","jagdish@gmail.com")
s1.display()

Student.test()
Student.sample()