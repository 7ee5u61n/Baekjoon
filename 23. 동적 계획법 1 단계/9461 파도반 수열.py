import sys
input = sys.stdin.readline

dp = [1]*101
for i in range(4, 101):
    dp[i] = dp[i-2]+dp[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])