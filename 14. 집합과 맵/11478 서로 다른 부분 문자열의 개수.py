import sys

S = list(sys.stdin.readline().rstrip())

partialString = {}

for i in range(len(S)):
    parts = S[i]
    partialString[parts] = 1
    for j in range(i+1, len(S)):
        parts += S[j]
        partialString[parts] = 1

# print(partialString)
print(len(partialString))