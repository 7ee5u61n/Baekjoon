n, m = map(int, input().split())
a = list(map(int, input().split()))

stress = 0
result = 0
for i in range(n):
    stress = max(0, stress + a[i])
    if stress >= m:
        result += 1
    
print(result)