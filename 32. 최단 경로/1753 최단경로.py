import heapq
import sys
INF = int(1e9)

# 정점의 개수, 간선의 개수
V, E = map(int, sys.stdin.readline().split())
# 시작 정점 번호
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    # u에서 v로 가는 가중치 w인 간선
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    # 경로가 존재하지 않을 경우
    if distance[i] == INF:
        print('INF')
    # 경로가 존재할 경우
    else:
        print(distance[i])