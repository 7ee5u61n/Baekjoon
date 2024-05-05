import sys

N, M = map(int, input().split()) # N개의 바구니, M번 공을 교환
N = list(range(1, N+1)) # 바구니의 번호와 같은 번호의 공이 들어있음

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split()) # i번째 바구니에 들어있는 공을 j번째 바구니에 있는 공과 교환
    N[i-1], N[j-1] = N[j-1], N[i-1]

result = " ".join(map(str, N)) # 공백으로 구분하여 한 줄에 출력
print(result)