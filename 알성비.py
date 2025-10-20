n = int(input())

high = 0
for _ in range(n):
    a, d, g = map(int, input().split())
    point = a*(d+g)
    if a == d+g:
        point *= 2

    high = max(high, point)

print(high)