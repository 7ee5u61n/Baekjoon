r, c = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

filter = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
count = 0
for i in range(r-2):
    for j in range(c-2):
        value = []
        for dx, dy in filter:
            value.append(pixel[i+dx][j+dy])
        value.sort()
        if value[4] >= t:
            count += 1

print(count)