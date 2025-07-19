n = int(input())
b = list(map(int, input().split()))

a = [0] * n

for i in range(n):
    a[i] = b[i]*(i+1)-sum(a[:i])

print(*a)