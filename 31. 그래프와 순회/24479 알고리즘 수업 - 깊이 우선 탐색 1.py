import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, start_node): # 인접 리스트, 시작 노드
    global count # 몇 번째 방문
    
    visited[start_node] = count

    for i in graph[start_node]:
        if visited[i] == 0: # 방문 안한 노드이면
            count += 1
            dfs(graph, i)

n, m, r = map(int, sys.stdin.readline().split()) # 정점의 수, 간선의 수, 시작 정점

graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1): # 오름차순으로 정렬
    graph[i].sort() 

visited = [0] * (n+1) # 0이면 방문 안 함
count = 1 # 몇 번째 방문

dfs(graph, r)

for i in range(1, n+1):
    print(visited[i])