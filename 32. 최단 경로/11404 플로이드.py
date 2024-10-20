INF = int(1e9)

# 도시의 개수
n = int(input())
# 도시를 연결하는 버스
m = int(input())
# 2차원 리스트 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 버스 정보
for _ in range(m):
    # a에서 b가는 비용 c
    a, b, c = map(int, input().split())
    # a에서 b까지 가는 가장 빠른 노선만 입력
    if graph[a][b] < c:
        continue
    else:
        graph[a][b] = c

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')

    print()