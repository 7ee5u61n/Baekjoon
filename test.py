x, y, p1, p2 = map(int, input().split())

result = -1
for _ in range(10001):
    if p1 < p2:
        p1 += x
    elif p1 > p2:
        p2 += y
    else:
        result = p1
        break

print(result)