N = int(input())
while N < 4 or N > 1000 or N % 4 != 0:
    print(' N은 4~1000 사이의 4의 배수')
    N = int(input())
howLong = N // 4

print('long '* howLong + 'int')