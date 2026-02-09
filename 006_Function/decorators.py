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


def get(a):
    print(a)

get("a")