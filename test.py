x0, n = map(int, input().split())
x = [x0]

for i in range(n+1):
    if x[i] % 2 == 0:
        x.append((x[i]//2)^6)
    else:
        x.append((2*x[i])^6)

print(x[n])