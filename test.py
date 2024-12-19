r, c = map(int, input().split())

arr = [list(input()) for _ in range(10)]

bomb = []
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'o':
            bomb.append((i, j))

for i, j in bomb:
    for k in range(10):
        arr[i][k] = 'o'
        arr[k][j] = 'o'

safe = []
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'x':
            safe.append((i+1, j+1))

min_move = 100
for i, j in safe:
    min_move = min(abs(r-i)+abs(c-j), min_move)

print(min_move)