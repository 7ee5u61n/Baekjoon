import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

arr = sorted(arr)
for i in range(n):
    print(arr[i])