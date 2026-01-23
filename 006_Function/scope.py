

# a = 10
def test():
    global a
    a = 20
    print(a)


test()
print(a)