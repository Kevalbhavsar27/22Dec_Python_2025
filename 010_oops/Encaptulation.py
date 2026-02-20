class Student : 
    
    __id  = 10

    def set(self,id):
        self.__id = id

    def get(self):
        print(self.__id)

s = Student()
s.set(20)
s.get()