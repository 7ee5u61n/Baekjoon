dp = ['1']*10001
for i in range(1, 10001):
    value = int(dp[i-1])*i
    
    while value % 10 == 0:
        value //= 10

    dp[i] = str(value)[-5:]

while True:
    try:
        n = str(input())
        result = dp[int(n)][-1]
        
        print(f'{' '*(5-len(n))}{n} -> {result}')
    
    except:
        break