n = int(input())

sqrt = int(n**0.5)
dp = [i for i in range(n+1)]

for i in range(2, sqrt+1):
    for j in range(i**2, n+1):
        if j -i**2 >= 0:
            dp[j] = min(dp[j], dp[j-i**2]+1)

print(dp[n])