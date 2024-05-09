import sys

T = int(input()) # 테스트 케이스의 개수
S = []

for _ in range(T):
    R,S = sys.stdin.readline().split() # 각 문자를 R번 반복. 문자열 S
    P = ''
    for i in range(len(S)):
        P += (S[i]*int(R))
    print(P)
