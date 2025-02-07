matrix = []
for i in range(5):
    matrix.append(input().split())
row = 0
columen = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':
            row = i
            column = j
result = abs(2 - row) + abs(2 - column)
print(result)
