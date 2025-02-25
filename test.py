n = int(input())

x = 0
y = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
lenth = 0
time = 0
for i in range(n):
    if i % 2 == 0:
        lenth += 1
    for j in range(lenth):
        x += dx[i%4]
        y += dy[i%4]
        time += 1
        if time == n:
            break
    if time == n:
        break

print(x, y)