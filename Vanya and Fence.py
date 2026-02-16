n, h = map(int, input().split())
heights = list(map(int, input().split()))
 
twidth = sum(2 if a > h else 1 for a in heights)
print(twidth)
