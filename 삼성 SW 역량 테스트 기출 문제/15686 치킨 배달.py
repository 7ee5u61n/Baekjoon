# 치킨집 폐업 횟수, 남은 치킨집
def dfs(count, temp):
    global result
    if count == len(chicken):
        if len(temp) == m:
            result = min(result, calc(temp))
        return

    dfs(count+1, temp+[chicken[count]])
    # 폐업
    dfs(count+1, temp)

def calc(temp):
    sum_distance = 0
    for r1, c1 in home:
        min_distance = INF
        for r2, c2 in temp:
            # 가장 가까운 치킨집 거리
            min_distance = min(min_distance, abs(r1-r2)+abs(c1-c2))
        sum_distance += min_distance

    return sum_distance

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        # 집
        if maps[i][j] == 1:
            home.append((i, j))
        # 치킨집
        elif maps[i][j] == 2:
            chicken.append((i, j))

INF = int(1e9)
result = INF
temp = []

dfs(0, temp)

print(result)