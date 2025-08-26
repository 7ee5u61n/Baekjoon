n = int(input())

mn = int(10e6)*6
result = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j > n:
            break
        for k in range(1, n+1):
            if i * j * k > n:
                break
            elif i*j*k == n:
                if 2*(i*j + j*k + k*i) < mn:
                    mn = 2*(i*j + j*k + k*i)
                    result = [i, j, k]
                
print(*result)