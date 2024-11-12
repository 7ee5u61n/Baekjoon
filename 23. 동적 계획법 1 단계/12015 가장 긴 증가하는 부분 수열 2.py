def binairy_search(target):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end)//2
    
        if LIS[mid] == target:
            return mid
        elif LIS[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


n = int(input())
a = list(map(int, input().split()))
LIS = [a[0]]
dp = [1]*(n)
for i in a:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = binairy_search(i)
        LIS[idx] = i

print(len(LIS))