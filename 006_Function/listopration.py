l = [2,5,9,8,7,15,420,26,560,98,520,41,560,52,25,100]

max = 0
smax = 0

for i in l : 
    if i>max:
        smax = max
        max= i
    elif i>smax and i!=max:
        smax =i


print(max)
print(smax)