T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    
    prev = min(a[0], n - a[0] + 1)
    flag = True
    for i in range(1, n):
        mini = min(a[i], n - a[i] + 1)
        maxi = max(a[i], n - a[i] + 1)
        
        if prev <= mini:
            prev = mini
        elif mini < prev <= maxi:
            prev = maxi
        elif maxi < prev:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')
    