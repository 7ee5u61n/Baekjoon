from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 시작점 삽입

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽뚫
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            # 괴물이다
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]

n, m = map(int, input().split()) # 세로, 가로

maze = [] # 미로 정보
for _ in range(n):
    maze.append(list(map(int, input()))) # 0: 괴물 있음, 1: 괴물 없음

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))