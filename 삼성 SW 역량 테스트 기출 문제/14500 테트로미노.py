def dfs(x, y, count, total):
    global result
    # 4번 더하면 종료
    if count == 4:
        result = max(result, total)
        return
    else:
        # 4방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 아직 방문 안했을 때
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                visited[nx][ny] = True
                # T노미노 만들기
                if count == 2:
                    dfs(x, y, count+1, total+maps[nx][ny])
                dfs(nx, ny, count+1, total+maps[nx][ny])
                # 재방문 하도록 초기화
                visited[nx][ny] = False

# 세로, 가로
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*(m) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, maps[i][j])
        visited[i][j] = False
print(result)