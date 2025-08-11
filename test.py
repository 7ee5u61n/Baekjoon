for i in range(1, 101):
    s = str(input())
    if s == 'Was it a cat I saw?':
        break

    for j in range(0, len(s), i+1):
        print(s[j], end='')
    print()