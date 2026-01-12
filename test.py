T = int(input())
for _ in range(T):
    n = int(input())
    n = bin(n)[2:]
    for i in range(len(n)-1, -1, -1):
        if n[i] == '1':
            print(len(n)-i-1, end=' ')
    print()