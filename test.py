n, m, a, b = map(int, input().split())

purchase = n*3-m
result = 0

if purchase > 0:
    result = purchase*a+b

print(result)