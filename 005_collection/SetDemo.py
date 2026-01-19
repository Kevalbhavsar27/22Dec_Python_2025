# s = {10,20,30,40,50,True,1,False,0}
# st = set((10,20,30))
# print(s)
# print(st)

# l = []
# print(type(l))
# t = ()
# print(type(t))
# s = set()
# print(type(s))

s = {10,20,30,40,50}

# for i in s:
#     print(i)

# s.add(100)
# print(s)

# s.update([10,20,30,40])
# print(s)

# t = (10,20,30,40,[10,20,30])
# t[4][0]=100
# print(t)

# s = {10,20,30,(10,20,30,30),(10,20,30)}
# print(s)


# s = {10,20,30,40}
# # s.remove(100)
# s.discard(100)
# print(s)


a = {10,20,30,40}
b = {20,30,40,50}

# a.update(b)
# c = a.union(b)
# c = a|b
# print(c)

# a.intersection_update(b)
# c = a.intersection(b)
# c = a&b
# print(c)

# a.difference_update(b)
# c = a.difference(b)
# c = b-a
# print(c)


# a.symmetric_difference_update(b)
# c = a.symmetric_difference(b)
# c = a^b
# print(c)


# f = frozenset({10,20,30,40})
# print(f)


# s = {10,20,30,45,78,89}
# s.pop()
# s.clear()
# del s
# print(s)

# k = s.copy()
# print(k)

a = {10,20,30,40,50}
b = {100,200}

print(a.issuperset(b))
print(b.issubset(a))
print(a.isdisjoint(b))