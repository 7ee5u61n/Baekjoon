# 중복 조합
from itertools import combinations_with_replacement

N, M = map(int, input().split())
N = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, combinations_with_replacement(N, M)))))