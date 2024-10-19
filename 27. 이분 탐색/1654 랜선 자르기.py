import sys

def cut_lan(array, start, end, n):
    global max_lenth

    if start > end:
        return max_lenth
    
    mid = (start + end) // 2
    
    # 만들 수 있는 랜선의 수
    count = 0
    for i in array:
        count +=  (i // mid)
    
    # n개를 만들 수 있을 때
    if count >= n:
        max_lenth =  mid
        return cut_lan(array, mid+1, end, n)
    # 필요한 수보다 적게 만들어 질 때
    else:
        return cut_lan(array, start, mid-1, n)
    
# 가지고 있는 랜선의 개수, 필요한 랜선의 개수
k, n = map(int, sys.stdin.readline().split())

# 랜선의 길이
lan = []
for i in range(k):
    lan.append(int(sys.stdin.readline()))

max_lenth = 0

print(cut_lan(lan, 1, max(lan), n))