import sys
N = int(sys.stdin.readline())

sum = 0
for i in range(N):
    P = int(sys.stdin.readline())
    if i != (N-1):
        sum += (P-1)
    else:
        sum += P

print(sum)