# l = [10,20,30,40,50]

# k = iter(l)
# print(next(k))
# print(next(k))

# print("ddsdsd")
# print("fdsf")

# print(next(k))


# def test():
#     yield "Hello"
#     yield "Test"

# k = test()
# print(next(k))
# print(next(k))

def square(a):
    for i in range(a):
        yield i*i
    
k = square(5)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
