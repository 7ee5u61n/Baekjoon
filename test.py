n, m = map(int, input().split())
paint = []
for _ in range(n):
    paint.append(list(input()))

for i in range(n):
    for j in range(m):
        if paint[i][j] != '.':
            paint[i][m-j-1] = paint[i][j]

for i in range(n):
    for j in range(m):
        print(paint[i][j], end='')
    print('')