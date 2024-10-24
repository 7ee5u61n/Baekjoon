def dfs(x, y, d):
    global count
    # 빈 칸 청소
    if graph[x][y] == 0:
        count += 1
        graph[x][y] = 2
    
    # 다음 진행 방향
    for i in range(1, 5):
        # 반시계 방향 회전
        nd = (d-i) % 4
        nx = x+dx[nd]
        ny = y+dy[nd]

        # 방 안
        if 0 <= nx < n and 0 <= ny < m:
            # 진행하는 방향에 빈칸이 있을 경우
            if graph[nx][ny] == 0:
                dfs(nx, ny, nd)
                return
    
    # 4방향 다 돌아도 빈 칸이 없을 때
    bd = (d+2)%4
    bx = x+dx[bd]
    by = y+dy[bd]
    
    # 뒤가 벽
    if graph[bx][by] == 1:
        return
    dfs(bx, by, d)

# 세로, 가로
n, m = map(int, input().split())

# 시작 좌표, 방향
r, c, d = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소한 칸
count = 0

dfs(r, c, d)

print(count)