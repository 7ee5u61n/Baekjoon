T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0]*(m+1)
    dp[0] = 1
    for i in coins:
        for j in range(i, m+1):
            dp[j] += dp[j-i]

    print(dp[m])