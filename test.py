a, b = map(int, input().split())

if a <= b:
    b = a-1
elif a > b:
    a = b+1

print(a+b)