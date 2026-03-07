m = list(map(int, input().split()))
n = int(input())

result = 0
for i in range(n):
    b, l, s = map(float, input().split())
    b = int(b)
    s = int(s)
    if s >= 17 and l >= 2.0:
        result += m[b]

print(result)