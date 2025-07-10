while True:
    s = str(input())
    if s == 'EOI':
        break

    found = False
    for i in range(len(s)-4):
        if s[i:i+4].upper() == 'NEMO':
            found = True
            break

    if found:
        print('Found')
    else:
        print('Missing')