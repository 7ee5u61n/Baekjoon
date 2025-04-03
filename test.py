def calc(a, b, c):
    value = 0
    if b == '+':
        value += a+c
    elif b == '-':
        value += a-c
    elif b == '*':
        value += a*c
    elif b == '/':
        value += int(a/c)

    return value

ko = list(map(str, input().split()))

k1 = int(ko[0])
o1 = ko[1]
k2 = int(ko[2])
o2 = ko[3]
k3 = int(ko[4])

value1 = calc(calc(k1, o1, k2), o2, k3)
value2 = calc(k1, o1, calc(k2, o2, k3))

print(min(value1, value2))
print(max(value1, value2))