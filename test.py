n, m = map(int, input().split())

a = list(input() for _ in range(n))
b = list(input() for _ in range(n))

result = True
for i in range(n):
    temp = ''        
    for j in range(m):
        temp += a[i][j]*2

    if temp != b[i]:
        result = False
        break

if result:
    print("Eyfa")
else:
    print("Not Eyfa")