import sys

def merge_sort(A):
    if len(A) <= 1:
        return A
    
    q = (len(A)+1)//2 # p, r의 중간 지점
    p = merge_sort(A[:q]) # 전반부 정렬
    r = merge_sort(A[q:]) # 후반부 정렬

    sorted_A = []
    l=h=0
    while l < len(p) and h < len(r):
        if p[l] <= r[h]:
            sorted_A.append(p[l])
            result.append(p[l])
            l += 1
        else:
            sorted_A.append(r[h])
            result.append(r[h])
            h += 1
    while l < len(p):
        sorted_A.append(p[l])
        result.append(p[l])
        l += 1
    while h < len(r):
        sorted_A.append(r[h])
        result.append(r[h])
        h += 1

    return sorted_A

result = []
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
merge_sort(A)

if len(result) >= K:
    print(result[K-1])
else:
    print(-1)