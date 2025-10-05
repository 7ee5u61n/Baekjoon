n = int(input())
if n == 0:
    print('divide by zero')
else:
    arr = list(map(int, input().split()))

    avg = sum(arr) / n
    
    exp = 0
    x = set(arr)
    for i in x:
        exp += i * arr.count(i)
    exp /= n
    
    if exp == 0:
        print('divide by zero')
    else:
        result = avg/exp
        print(f'{result:.2f}')