# def before(func):
#     def exec():
#         print("pring before test")
#         func()
#         print("pringing after function")
#     return exec
# @before
# def test():
#     print("test calling...")

# test()

def add(func):
    def exec(*a):
        print(f"addition of {a[0]} and {a[1]} is{a[0]+a[1]}")
        func(*a)
    return exec

def mul(func):
    def exec(*a):
        print(f"multiplication of {a[0]} and {a[1]} is{a[0]*a[1]}")
        func(*a)
    return exec

# @add
# @mul
# def calc(a,b):
#     print("calc calling")

# calc(10,20)

def numbersOnly(func):
    def execute(a):
        if  str(a).isdigit():
           func(a) 
        else :
            print("invalid data")      
    return execute

def charOnly(func):
    def execute(a):
        if  str(a).isalpha():
           func(a) 
        else :
            print("invalid data")
       
    return execute


def get(a):
    print(a)

get("fddff")