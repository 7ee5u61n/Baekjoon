import sys

n, k = map(int, sys.stdin.readline().split())
visited = set()
dabbada = set()

dx = [2, -2, 0, 0]
dy = [0, 0, 2, -2]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    dabbada.add((x, y))

for x, y in dabbada:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx <= n and 0 < ny <= n:
            if (nx, ny) not in visited and (nx, ny) not in dabbada:
                visited.add((nx, ny))
      
print(len(visited))