import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

# 정점의 개수, 간선의 개수
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(e):
    a, b, c = map(int, input().split())
    # 양방향 간선
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

distance1 = dijkstra(1)
distancev1 = dijkstra(v1)
distancev2 = dijkstra(v2)

path1 = distance1[v1] + distancev1[v2] + distancev2[n]
path2 = distance1[v2] + distancev2[v1] + distancev1[n]

result = min(path1, path2)
if result < INF:
    print(result)
else:
    print(-1)