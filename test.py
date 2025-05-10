while True:
    n = int(input())
    if n == 0:
        break
    
    arr = [str(input()) for _ in range(n)]
    arr.sort(key= lambda x: x.upper())
    
    print(arr[0])