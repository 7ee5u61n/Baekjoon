while True:
    s = str(input())
    a = s[0]
    if a == '#':
        break
    b = s[2:].lower()

    result = 0
    for i in b:
        if i == a:
            result += 1

    print(f'{a} {result}')