import sys

N = list(sys.stdin.readline().rstrip())
N.sort(reverse=True)

sys.stdout.write(''.join(N))