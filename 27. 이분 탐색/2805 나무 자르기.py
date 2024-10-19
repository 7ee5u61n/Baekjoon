import sys

def binary_search(array, start, end, value):
    
    # 절단기 최대 높이
    global max_cut
    
    # 끝까지 정확히 가져갈 수 없는 경우
    if start > end:
        return max_cut

    mid = (start+end) // 2
    
    cut = 0
    for i in range(n):
        # 자를 수 있을 때
        if array[i] - mid > 0:
            # 가져갈 나무
            cut += array[i] - mid
    
    if cut == value:
        return mid
    elif cut < value:
        return binary_search(array, start, mid-1, value)
    else:
        max_cut = mid
        return binary_search(array, mid+1, end, value)

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

max_cut = 0
print(binary_search(trees, 0, max(trees), m))