T = int(input())
for _ in range(T):
    m, p = input().split()

    if p == 'C':
        arr = list(map(str, input().split()))
        for i in arr:
            print(ord(i)-64, end=' ')
        print('')

    else:
        arr = list(map(int, input().split()))
        for i in arr:
            print(chr(i+64), end=' ')
        print('')