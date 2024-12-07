def intergration(x, a, b, c, d, e):
    return (((a*x**3)//3) + ((b*x**2)//2) + (c*x)) - (((d*x**2)//2) + (e*x))

x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

power = intergration(x2, a, b, c, d, e) - intergration(x1, a, b, c, d, e)
print(power)