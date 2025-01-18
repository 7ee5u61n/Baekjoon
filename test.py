while True:
    s = str(input())
    if s == '0':
        break
    
    print(s, end=' ')
    while len(s) > 1:
        value = 1
        for i in s:
            value *= int(i)
        s = str(value)

        print(s, end=' ')

    print('')