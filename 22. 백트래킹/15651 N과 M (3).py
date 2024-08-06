from itertools import product

N, M = map(int, input().split())
N = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, product(N, repeat=M)))))