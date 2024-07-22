import sys

for _ in range(3):
    S = 0
    N = int(sys.stdin.readline())
    for i in range(N):
        S += int(sys.stdin.readline())
    if S == 0:
        sys.stdout.write('0'+ '\n')
    elif S >= 0:
        sys.stdout.write('+' + '\n')
    else:
        sys.stdout.write('-' + '\n')