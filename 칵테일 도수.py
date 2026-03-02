import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    if n ** 0.5 == int(n ** 0.5):
        print(1)
    else:
        print(0)