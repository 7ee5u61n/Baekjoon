dp = [0]*101
dp[1] = 1

for i in range(2, 101):
    dp[i] = dp[i-1]+i**2

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n])