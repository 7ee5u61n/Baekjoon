n, k = map(int, input().split())
g = list(map(int, input().split()))

for i in range(k):
    p = g[i]*100//n
    if 0 <= p <= 4:
        print(1, end=' ')
    elif 4 < p <= 11:
        print(2, end=' ')
    elif 11 < p <= 23:
        print(3, end=' ')
    elif 23 < p <= 40:
        print(4, end=' ')
    elif 40 < p <= 60:
        print(5, end=' ')
    elif 60 < p <= 77:
        print(6, end=' ')
    elif 77 < p <= 89:
        print(7, end=' ')
    elif 89 < p <= 96:
        print(8, end=' ')
    elif 96 < p <= 100:
        print(9, end=' ')
