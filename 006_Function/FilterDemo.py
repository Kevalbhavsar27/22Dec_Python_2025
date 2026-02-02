# l = [4,5,6,9,8,4,54,23,24,27,45,97]

# def checkodd(a):
#     if a%2!=0:
#         return a   
# k = []
# for i in l:
#     o = checkodd(i)  
#     if o is not None:
#         k.append(o)

# k = filter(checkodd,l)

# k = filter(lambda a  :a%2!=0,l)
# print(list(k))

# subjects = ["python","java","php","android"]
# # k = filter(lambda i:"a" in i , subjects)
# k = filter(lambda i:i.startswith('a') , subjects)
# print(list(k))

# k = filter(lambda a : a>10 and a<50,l)
# print(list(k))

d = {"pyhon":30,"java":15,"node":45,"react":35,"php":60}
k = {}

def test(a):
    if a[1]>30:
        return {a[0]:a[1]}

# for i in d.items() : 
#     t = test(i)
#     if t is not None:
#         k.update(t)
k = filter(test,d.items())
print(dict(k))
    


  



# def test(a):
#     if a[1]>30:
#         return a

# k = filter(test,d.items())
# print(list(k))



