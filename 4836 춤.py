def power(a, b):
    if b == 0:
        return 1

    x = power(a, b//2)

    if b % 2 == 0:
        return x*x
    else:
        return a*x*x
    
n = int(input())
l = str(input())
r = 31
m = 1234567891

h = 0
for i in range(n):
    a = ord(l[i])-96
    h += (a*power(r, i))

print(h%m)