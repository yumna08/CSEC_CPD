n = input()
lower = 0
upper = 0
for i in n:
    if i.islower():
        lower += 1
    else:
        upper += 1
if lower >= upper:
    print(n.lower())
else:
    print(n.upper())
  
