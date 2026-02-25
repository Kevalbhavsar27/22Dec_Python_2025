# class Sample:

#     def __str__(self):
#         return "This is sample class object"
# s  =Sample()
# print(s)



# class Calc:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b

# c = Calc(10,20)
# k = Calc(10,20)
# print(c==k)

class Test:

    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
    def __setitem__(self, key, value):
        self.l[key]=value

    def __getitem__(self, key):
        return self.l[key]


t = Test([10,20,30,40])
# print(len(t))
t[2]=400
print(t.l)
print(t[0])