INF = int(1e9)

# 마을, 도로
v, e = map(int, input().split())

graph = [[INF]*(v+1) for _ in range(v+1)]

for a in range(1, v+1):
    for b in range(1, v+1):
        if a == b:
            graph[a][b] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, v+1):
    print(graph[i])