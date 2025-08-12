import math

def solve():
    a, b, c = map(int, input().split())
    
    p = a
    q = 2 * b * c
    r = a * (c * c - a * a + b * b)

    d = q * q - 4 * p * r

    if d < 0:
        print("-1")
        return

    x = (-q + math.sqrt(d)) / (2 * p)

    if x < 0:
        print("-1")
        return

    result = int(x)
    print(result)

solve()