INF = int(1e6)

n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))

dp = [INF]*(k+1)
dp[0] = 0

for coin in coins:
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])