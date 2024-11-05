T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    # 아래 층
    base = [i for i in range(n+1)]
    # 현재 층
    dp = [1]*(n+1)
    for i in range(1, k+1):
        for j in range(1, n+1):
            # 1호는 항상 1명
            if j == 1:
                dp[j] = 1
            # n-1호 + 아래집
            else:
                dp[j] = dp[j-1] + base[j]
        base = dp

    print(dp[n])
