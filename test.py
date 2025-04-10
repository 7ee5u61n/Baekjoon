import math

a, b, c = map(int, input().split())
t = int(input())

if t <= 30:
    print(a)
else:
    a += math.ceil((t-30)/b)*c
    print(a)