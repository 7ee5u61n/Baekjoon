n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] += dp[i-1]+arr[i-1]
    
result = -(100*100000)
for i in range(1, n-k+2):
    sm = dp[i+k-1] - dp[i-1]
    if result < sm:
        result = sm

print(result)