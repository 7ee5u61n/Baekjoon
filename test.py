n, x = map(int, input().split())

bus = [list(map(int, input().split())) for _ in range(n)]
bus.sort()

result = -1
for s, t in bus:
    if s+t <= x:
        result = s

print(result)