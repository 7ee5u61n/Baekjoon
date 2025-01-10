T = int(input())
for _ in range(T):
    n = str(input())
    
    count = 0
    while n != '6174':
        count += 1
        arr = []
        for i in n:
            arr.append(i)
        
        mx = int(''.join(sorted(arr, reverse=True)))
        mn = int(''.join(sorted(arr)))

        if mx-mn < 1000:
            n = '0' + str(mx-mn)
        else:
            n = str(mx-mn)
    
    print(count)