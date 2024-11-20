import sys
sys.setrecursionlimit(int(1e6))

def dfs(x, y):
    global dp
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < m and 0 <= ny < n:
                # 내리막인 경우
                if maps[nx][ny] < maps[x][y]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]


m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dp = [[-1]*(n) for _ in range(m)]

print(dfs(0, 0))