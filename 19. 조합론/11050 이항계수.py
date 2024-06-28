import sys
N, K = map(int, input().split())

if K == 0:
    print(1)
    sys.exit()

result = 1
for _ in range(K):
    result *= N
    N -= 1
for _ in range(K):
    result //= K
    K -= 1

print(result)