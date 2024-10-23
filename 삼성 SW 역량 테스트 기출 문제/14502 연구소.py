from collections import deque
from itertools import combinations

# 바이러스 퍼짐
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 연구소 안
        if 0 <= nx < n and 0 <= ny < m:
            # 바이러스 퍼질 수 있을 때
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                # 바이러스 있는 칸에서 시작
                if temp[i][j] == 2:
                    virus(i, j)
        
        safe = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    safe += 1
        result.append(safe)
        
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
    
n, m = map(int, input().split())
graph = []
temp = [[0]*m for _ in range(n)]

# 바이러스 전염 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 안전한 칸들의 개수
result = []

dfs(0)

print(max(result))