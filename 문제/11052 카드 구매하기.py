n = int(input())
cards = [0] + list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if j - i >= 0:
            dp[j] = max(dp[j], dp[j-i]+cards[i])

print(dp[n])