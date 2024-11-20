d = [0]*1001

for i in range(1001):
    if i == 1:
        d[i] = 1
    elif i == 2:
        d[i] = 2
    else:
        d[i] = (d[i-1] + d[i-2])

n = int(input())
print(d[n]%10007)