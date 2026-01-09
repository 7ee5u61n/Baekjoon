T = int(input())
for _ in range(T):
    n = int(input())
    print('++++ '*(n//5), end='')
    print('|'*(n%5))