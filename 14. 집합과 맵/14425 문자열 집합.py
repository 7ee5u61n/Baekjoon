N, M = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())
S = set(S)

checkStr = []
for _ in range(M):
    checkStr.append(input())

count = 0
for i in range(M):
    if checkStr[i] in S:
        count += 1

print(count)