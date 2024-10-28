def dfs(day, earn):
    global max_earn
    
    # 날짜 지남
    if day >= n:
        max_earn = max(earn, max_earn)
        return
    
    if day+plan[day][0] <= n:
        dfs(day+plan[day][0], earn+plan[day][1])
    
    dfs(day+1, earn)

n = int(input())
plan = [list(map(int, input().split())) for _ in range(n)]

max_earn = 0
dfs(0, 0)

print(max_earn)