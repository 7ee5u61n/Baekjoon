n = int(input())
point = []
for i in range(1, n+1):
    s, c, l = map(int, input().split())
    point.append((s, c, l, i))

point.sort(key=lambda x: (-x[0], x[1], x[2]))

print(point[0][3])