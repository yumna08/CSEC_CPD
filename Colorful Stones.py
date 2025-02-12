a = input()
b = input()

n = 0 

for i in range(len(b)):  
    if b[i] == a[n]:  
        n += 1  
        if n == len(a):  
            break  

print(n + 1) 
