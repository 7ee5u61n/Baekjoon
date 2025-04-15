dp = [0]*65
dp[1] = 1

for i in range(2, 65):
    dp[i] = dp[i-1]*2

n = int(input())

count = 0
for i in range(65):
    if n <= dp[i]:
        count = i
        n -= dp[i]
        break

print(count)