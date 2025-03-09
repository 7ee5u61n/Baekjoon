n, m = map(int, input().split())

garden = [[0]*(m+1) for _ in range(n+1)]

row = list(map(int, input().split()))
col = list(map(int, input().split()))

for i in range(n):
    garden[i+1][0] = row[i]
for i in range(m):
    garden[0][i+1] = col[i]

for i in range(1, n+1):
    for j in range(1, m+1):
        if garden[i-1][j] == garden[i][j-1]:
            garden[i][j] = 0
        else:
            garden[i][j] = 1

print(garden[n][m])