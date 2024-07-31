def howLong(x): # x = str
    width = 0
    for i in range(len(x)):
        if x[i] == '0':
            width += 4
        elif x[i] == '1':
            width += 2
        else:
            width += 3
    width += (len(x)+1)
    return width
while True:
    N = str(input())
    if N == '0':
        break
    print(howLong(N))