# x, y, 단지별 집의 수
def dfs(x, y):
    global count
    # 단지 번호 붙인 집
    graph[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                dfs(nx, ny)
                count += 1

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 각 단지내 집 수를 나타내는 리스트
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 1
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)