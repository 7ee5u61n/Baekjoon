from collections import deque

def bfs(graph, start):
    global count

    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                count += 1
                q.append(i)

    return count

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, (input().split()))
    graph[a].append(b)
    graph[b].append(a)

count = 0

print(bfs(graph, 1))