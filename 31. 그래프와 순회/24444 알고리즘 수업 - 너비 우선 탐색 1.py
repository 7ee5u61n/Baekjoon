import sys
from collections import deque

# 정점의 수, 간선의 수, 시작 정점
n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬
for i in range(n+1):
    graph[i].sort()

visited = [0] * (n+1)
count = 1

def bfs(graph, start, visited):
    
    global count

    queue = deque([start])
    visited[start] = count

    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                count += 1
                queue.append(i)
                visited[i] = count

bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])