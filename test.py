import sys


n, k = map(int, sys.stdin.readline().split())
board = {}

dx = [2, -2, 0, 0]
dy = [0, 0, 2, -2]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[(x, y)] = -1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n and 0 <= ny <= n:
            if (nx, ny) in board and board[(nx, ny)] == -1:
                continue
            else:
                board[(nx, ny)] = 1

count = 0
for x, y in board.items():
    if y != -1:
        count += 1

print(count)