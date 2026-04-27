n = int(input())
result = -1
for _ in range(n):
    a, b, c = map(int, input().split())
    if a+b+c >= 512:
        if result == -1 or result > a+b+c:
            result = a+b+c

print(result)