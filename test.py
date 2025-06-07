import math

coord = [dict() for _ in range(4)]
dist = [[0.0] * 4 for _ in range(4)]
visit = [False] * 4
result = int(1e6)

def dfs(index, total, count):
    global result
    if count == 4:
        result = min(result, int(total))
        return
    
    if visit[index]:
        return
    
    visit[index] = True
    for i in range(4):
        dfs(i, total + dist[index][i], count + 1)
    visit[index] = False

for i in range(4):
    x, y = map(int, input().split())
    coord[i]['x'], coord[i]['y'] = x, y

for i in range(4):
    x, y = coord[i]['x'], coord[i]['y']
    for j in range(i + 1, 4):
        nx, ny = coord[j]['x'], coord[j]['y']
        d = math.sqrt((x - nx) ** 2 + (y - ny) ** 2)
        dist[i][j] = dist[j][i] = d

dfs(0, 0.0, 0)

print(result)