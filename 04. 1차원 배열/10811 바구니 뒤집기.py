import sys

N, M = map(int, input().split()) # N개의 바구니, M번 바구니를 교환
N = list(range(1, N+1)) # N번 까지 바구니 배열

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split()) # i번째 부터 j번째 까지 바구니 순서를 역순으로 만듦
    N[i-1:j] = N[i-1:j][::-1]
print(*N)