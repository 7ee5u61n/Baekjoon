N = int(input())

n = 2
a = 1

for i in range(N):
    n += a
    a *= 2
    D = n**2 

print(D)