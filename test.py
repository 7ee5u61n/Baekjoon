while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    square = []
    for i in range(1, 151):
        for j in range(i, 151):
            if i == j:
                continue
            else:
                square.append([(i**2+j**2), i, j])

    square = sorted(square, key=lambda x: (x[0], x[1]))
    result = square[square.index([h**2+w**2, h, w])+1]
    print(result[1], result[2])