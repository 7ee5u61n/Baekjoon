def dfs(x, y):
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]

    crash = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if map[nx][ny] == 'X':
            crash += 1
        elif map[nx][ny] == '#':
            return
    
    park[crash] += 1

r, c = map(int, input().split())
map = list(list(input()) for _ in range(r))

park = [0]*5
for i in range(r-1):
    for j in range(c-1):
        dfs(i, j)

for i in park:
    print(i)