def dfs(s):
    global result
    if len(s) == m:
        result.append(s)
        return
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            dfs(s+[i])
            visited[i] = False
        
n, m = map(int, input().split())

visited = [False]*(n+1)
result = []
dfs([])

for i in result:
    print(*i)