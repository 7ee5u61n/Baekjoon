n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[1])
else:
    d = [0]*(n+1)
    d[1] = stairs[1]
    d[2] = stairs[1]+stairs[2]
    for i in range(3, n+1):
        d[i] = max(d[i-3]+stairs[i-1], d[i-2]) + stairs[i]
    print(d[n])