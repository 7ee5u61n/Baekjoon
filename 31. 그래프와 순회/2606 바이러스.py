def dfs(graph, start):
    global count

    visited[start] = True

    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            count += 1
            dfs(graph, i)
    
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

print(dfs(graph, 1))