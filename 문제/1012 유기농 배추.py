import sys
sys.setrecursionlimit(int(1e6))

def dfs(y, x):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if maps[ny][nx] == 1:
                maps[ny][nx] = 0
                dfs(ny, nx)
    

T = int(input())
for test_case in range(1, T+1):
    m, n, k = map(int, input().split())
    maps = [[0]*m for _ in range(n)]
    
    cabbage = []
    for _ in range(k):
        x, y = map(int, input().split())
        cabbage.append((y, x))
        maps[y][x] = 1

    count = 0
    for y, x in cabbage:
        if maps[y][x] == 1:
            count += 1
            dfs(y, x)

    print(count)