n = int(input())

a = 1
b = 1
for i in range(n-1):
    if a == 1:
        a = b+1
        b = 1
    else:
        a -= 1
        b += 1

print(a, b)