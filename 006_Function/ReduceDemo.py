from functools import reduce

# l = [10,20,30,40,50,60]

# def sum(a,b):
#     print(a,b)
#     return a+b


# k = reduce(sum,l)
# k = reduce(lambda a,b : a+b,l)
# print(k)

# l = [2,5,9,8,7,15,26,56,98,41,52,25,100]

# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b   
# k = reduce(max,l)

k = reduce(lambda a,b : a if a>b else b,l)
print(k)