# l = [10,20,30,40,50,50,"abc",45.56,True]

# print(l)
# print(len(l))
# print(type(l))

# k = list((10,203))
# print(k)


#access list
# l = ["java","python","node","php","java"]
# print(l[0])
# print(l[-1])
# print(l[1:3])
# print(l[::-1])
# print("java" in l)

#change list item

# l[0] = "React"
# l[1:3] = [""]
# l.insert(2,"XYZ")
# l.append("XYZ")
# k = [10,20,30]
# l.extend(["A","B"])
# l.extend(k)

#Remove item

# l.remove("java")
# l.pop()
# l.pop(2)
# l.clear()
# del l
# print(l)

#looping

l = [10,20,30,40,50]
# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1



#comprehention

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# k = []
# for i in fruits:
#     if "a" in i:
#         k.append(i)

# k = [i for i in fruits if "a" in i]
# k = [i for i in fruits if i.startswith("a")]
# k = ["abc" for i in fruits]
# print(k)


l = [10,2,5,60,45,89,26,54]

# l.sort()
# k=sorted(l)

# l.sort(reverse=True)
# l.reverse()
# print(l)

# k = l
# k = l.copy()
# k = list(l)
# k = l[:]
# print(k)

a = [10,20,30,10,10,"abc"]
b = [100,200,300]
# c  =a+b
# a.extend(b)
# print(a)

# print(a.count(10))

# print(a.index(10))
# print(max(a))
# print(min(a))

l = [[10,20],[30,40],[50,60]]
for i in l:
    for j in i:
        print(j)