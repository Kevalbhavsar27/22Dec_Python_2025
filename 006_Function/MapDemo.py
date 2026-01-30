# l = [10,20,30,40,50,60]
# k = []
# def square(a):
#     return a*a
# for i in l:
#     sq = square(i)
#     k.append(sq)
# k = map(square,l)

# k = map(lambda a:a*a,l)
# print(list(k))

# a = [10,20,30,40,50,60]
# b = [1,2,3,4,5]

# k = map(lambda x,y : x*y ,a,b)
# print(list(k))

subjects = ["python","java","php","android"]
k = map(lambda a:len(a), subjects)
print(list(k))