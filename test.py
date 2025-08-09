import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
l = list(map(int, input().split()))
c = list(map(str, input().split()))

result = False
for i in range(n):
    for j in range(i+1, n):
        if abs(x[i]-x[j]) <= l[i]+l[j] and c[i] != c[j]:
            result = True
            break
    if result:
        break

if result:
    print("YES")
    print(i+1, j+1)
else:
    print("NO")