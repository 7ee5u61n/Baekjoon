import math

n = int(input())
m = int(input())
x = list(map(int, input().split()))

result = x[0]
for i in range(1, m):
    value = math.ceil((x[i]-x[i-1])/2)
    result = max(result, value)
result = max(result, n-x[-1])

print(result)