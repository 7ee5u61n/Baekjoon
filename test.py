n = int(input())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

x = ''
y = ''

for i in range(n):
    x += a[i]
    y += b[i]

x = int(x)
y = int(y)

if x < y:
    print(x)
elif x >= y:
    print(y)