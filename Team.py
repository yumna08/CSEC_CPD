x=int(input())
total=0
for i in range(x):
    a=input()
    if a.count("1")>=2:
        total=total+1
print(total)
        
