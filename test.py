n = int(input())
a, b = map(int, input().split())

beverages = a//2+b

if n > beverages:
    print(beverages)
else:
    print(n)
    