import sys

# N = N까지의 자연수, M = 뽑는 갯수, A = 수열, C = 이미 고른 것
def pick(N, M, A, C):
    if len(A) == M:
        print(*A)
        return
    for i in range(1, N+1):
        if C[i]:
            continue
        C[i] = True
        A.append(i)
        pick(N, M, A, C)
        A.pop()
        C[i] = False

N, M = map(int, sys.stdin.readline().split())

arr = []
check = [False] * (N+1)

pick(N, M, arr, check)