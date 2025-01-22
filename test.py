dp = [1]*31

for i in range(30):
    dp[i+1] = dp[i]*2

n = int(input())

if n in dp:
    print(1)
else:
    print(0)