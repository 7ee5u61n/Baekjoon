n, m = map(int, input().split())
preference = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            value = 0
            for l in range(n):
                value += max(preference[l][i], preference[l][j], preference[l][k])
            result = max(value, result)

print(result)