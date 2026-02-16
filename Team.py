or _ in range(n):
    views = list(map(int, input().split()))
    if sum(views) >= 2:
        solved_count += 1
print(solved_count)
