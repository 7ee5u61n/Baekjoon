import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
# N = N까지의 자연수, M = 뽑는 갯수
def pick(start):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(start, N+1):
        if i in arr:
            break
        else:
            arr.append(i)
            pick(i+1)
            arr.pop()
            
pick(1)