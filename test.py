dp = [1]*10001
for i in range(3, 10001):
    dp[i] = dp[i-2]+dp[i-1]

n = int(input())
print(dp[n])