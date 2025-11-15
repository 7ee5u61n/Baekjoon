n, m = map(int, input().split())

result = []
for i in range(1000):
    for j in range(1000):
        if i + j == n and i - j == m:
            result = [i, j]
            break
result = sorted(result, reverse=True)
if result:
    print(*result)
else:
    print(-1)