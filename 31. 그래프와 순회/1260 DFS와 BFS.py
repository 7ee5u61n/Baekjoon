from collections import deque

def dfs(graph, v, visited):
    global dfs_result
    # 시작 노드
    if visited[v] == False:
        visited[v] = True
        dfs_result.append(v)

    for i in graph[v]:
        # 방문하지 않았다면
        if visited[i] == False:
            visited[i] = True
            # 방문 노드 출력
            dfs_result.append(i)
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    global bfs_result
    bfs_result = [start]
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                bfs_result.append(i)
                q.append(i)

# 정점의 개수, 간선의 개수, 시작 정점 번호
n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

# 그래프 정렬
for i in range(n+1):
    graph[i].sort()
 
dfs_result = []
bfs_result = []
# dfs 수행
dfs(graph, v, visited)
visited = [False] * (n+1)
# bfs 수행
bfs(graph, v, visited)

#dfs 결과 출력
for i in dfs_result:
    print(i, end=' ')
print()

# bfs 결과 출력
for i in bfs_result:
    print(i, end=' ')