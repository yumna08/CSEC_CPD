n = int(input())
a = input()
stone = 0
for i in range(1,len(a)):
    if a[i] == a[i-1]:
               stone += 1
print(stone)
