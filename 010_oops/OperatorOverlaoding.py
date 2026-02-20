class Sample : 

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a+other.a,self.b+other.b

    def __mul__(self, other):
        return self.a*other.a,self.b*other.b

s = Sample(10,20)
s1 = Sample(30,40)

# k = s+s1
# print(k)

k = s*s1
print(k)