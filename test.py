import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [0]*(n+1)

for _ in range(q):
    l, p, x = map(int, input().split())

    if l == 1:
        arr[p] += x
    elif l == 2:
        print(sum(arr[p:x+1]))
    