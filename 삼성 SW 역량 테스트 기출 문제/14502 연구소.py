def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def dfs(wall):
    global result
    if wall >= 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = maps[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        safe = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    safe += 1
        
        result = max(result, safe)
        return
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall += 1
                dfs(wall)
                maps[i][j] = 0
                wall -= 1


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

dfs(0)

print(result)