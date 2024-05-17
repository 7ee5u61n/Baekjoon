matrix = [[0 for col in range(9)] for row in range(9)] # 9*9 크기의 행렬

for i in range(9):
    value = list(map(int, input().split())) # 행렬의 값 입력
    for j in range(9):
        matrix[i][j] = value[j]

max = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if max < matrix[i][j]:
            max = matrix[i][j]
            row = i+1
            col = j+1
        elif max == 0:
            row = 1
            col = 1

print(max)
print(row,col)