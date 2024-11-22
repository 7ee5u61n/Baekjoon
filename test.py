n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

taxi = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            taxi.append((i, j))

distance = abs(taxi[1][0] - taxi[0][0]) + abs(taxi[1][1] - taxi[0][1])
print(distance)