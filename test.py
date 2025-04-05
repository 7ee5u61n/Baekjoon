n, k = map(int, input().split())

num = ''
for i in range(n*5):
    num += format(i, 'b')

for i in range(5):
    print(num[(k+i*n-1)], end=' ')