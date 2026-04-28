n, k, t = map(int, input().split())
d = list(map(int, input().split()))
t = [t]
result = 0
for i in range(n):
    if t[i] > k:
        t.append(t[i]+d[i]-abs(t[i]-k))
    elif t[i] < k:
        t.append(t[i]+d[i]+abs(t[i]-k))
    else:
        t.append(t[i]+d[i])
    result += abs(t[-1]-k)

print(result)