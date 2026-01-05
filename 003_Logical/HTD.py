number = "90"
a = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
p=0
sum = 0
for i in range(len(number)-1,-1,-1):
    sum +=(a.index(number[i])*(16**p))
    p+=1

print(sum)