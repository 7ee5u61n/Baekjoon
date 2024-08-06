from itertools import permutations

N, M = map(int, input().split())
N = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, permutations(N, M)))))