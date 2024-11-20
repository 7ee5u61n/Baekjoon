n, m = map(int, input().split())
maps = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    maps[i] = [0] + list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        # 현재칸의 사탕 최댓값은 왼쪽, 위, 왼쪽위의 최댓값 + 현재칸 사탕 개수
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maps[i][j]

print(dp[n][m])