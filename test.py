def snow(size, index, count):
    global result

    if count > m:
        return
    
    if count <= m:
        result = max(result, size)
    
    if index + 1 <= n:
        snow(size+a[index+1], index+1, count+1)
    if index + 2 <= n:
        snow(size//2+a[index+2], index+2, count+1)

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

result = -1
snow(1, 0, 0)
print(result)