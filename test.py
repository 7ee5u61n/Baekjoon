n, m = map(int, input().split())
box = 0
if n:
    book = list(map(int, input().split()))
    box = 1
    weight = 0
    for i in range(n):
        if book[i] + weight <= m:
            weight += book[i]
        else:
            weight = book[i]
            box += 1
    
print(box)