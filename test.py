n, m = map(int, input().split())
candidate = list(input() for _ in range(n))

result = 0
for i in candidate:
    o = 0
    x = 0
    for j in i:
        if j == 'O':
            o += 1
        else:
            x += 1

    if o > x:
        result += 1

print(result)