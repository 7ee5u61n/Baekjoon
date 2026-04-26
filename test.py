a, b, c = map(int, input().split())

if a == 0:
    a = c**2 - b
    print(int(a))
elif b == 0:
    b = c**2 - a
    print(int(b))
else:
    c = (a + b)**0.5
    print(int(c))