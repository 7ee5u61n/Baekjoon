n = int(input())

result = int(1e6)
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        result = min(result, b)

if result > 1000:
    print(-1)
else:
    print(result)