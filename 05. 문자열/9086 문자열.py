import sys

T = int(input()) # 테스트 케이스 개수 T

for _ in range(T):
    S = list(map(str, sys.stdin.readline().rstrip())) # 단어 S
    print(S[0]+S[-1])