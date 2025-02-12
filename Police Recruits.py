n = int(input(""))
a = list(map(int, input("").split()))
police = 0
crime = 0
for i in range(n):
    if a[i] == -1 and police == 0:
        crime +=1
    elif a[i] ==-1 and police != 0:
        police -=1
    elif a[i] !=-1:
        police += a[i]

print (crime)
