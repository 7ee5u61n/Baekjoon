while True:
    N = int(input())
    if 1 <= N <= 100:
        break

for i in range(N-1):
    i += 0
    print(' ' * (N-i-1) + '*' * (2 * i + 1))
print('*' * (2 * N - 1))
for i in range(N-1):
    i += 0
    print(' ' * (i+1) + ('*' * (2*(N-i-1)-1)))