n = int(input())

cards = list(map(int, input().split()))

p1 = 0
p2 = 0
left = 0
right = n - 1
turn = 0

while left <= right:
    if cards[left] > cards[right]:  
        card = cards[left]
        left += 1
    else:
        card = cards[right]
        right -= 1
    
    if turn % 2 == 0: 
        p1 += card
    else:  
        p2 += card
    
    turn += 1 

print(p1, p2)
