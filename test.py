n = int(input())
m = list(map(int, input().split()))

for i in range(n):
    if m[i] == 300:
        print(1, end=' ')
    elif m[i] >= 275:
        print(2, end=' ')
    elif m[i] >= 250:
        print(3, end=' ')
    else:
        print(4, end=' ')

