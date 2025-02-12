count = 0
n = int(input())
l = 0
for i in range(n):
    a = input()
    if(a != l):
        count += 1
    l = a
print(count)
