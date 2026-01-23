
def square(a):
    print(a*a)
    a+=1
    if a<=10:
        square(a)

square(1)