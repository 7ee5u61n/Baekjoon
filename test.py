import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    result = 0
    for _ in range(n):
        result += max(0, max(list(map(int, input().split()))))
    print(result)