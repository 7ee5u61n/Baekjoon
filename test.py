a = list(input())
b = set(input().split())

for i in range(len(a)):
    if a[i] in b:
        a[i] = a[i].lower()

for i in a:
    print(i, end='')